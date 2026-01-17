from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

# ------------------ Text-to-Speech ------------------ #
def speak(str1):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(str1)

# ------------------ Video & Face Detector ------------------ #
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# ------------------ Load Labels & Faces ------------------ #
with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix --> ', FACES.shape)

# ------------------ Train KNN ------------------ #
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# ------------------ Load Background ------------------ #
bg_path = '/mnt/data/eaa15bfd-ba05-488d-a17d-85ef82f499cc.png'
imgBackground = cv2.imread(bg_path)
if imgBackground is None:
    print("Error: background image not found!")
    exit()

# Resize background to match video frame placement
imgBackground = cv2.resize(imgBackground, (750, 650))  # adjust if needed

# ------------------ CSV Columns ------------------ #
COL_NAMES = ['NAME', 'TIME']

# ------------------ Main Loop ------------------ #
while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    attendance = None

    for (x, y, w, h) in faces:
        # Crop face & resize for KNN
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)

        # Predict name
        output = knn.predict(resized_img)
        person_name = str(output[0])

        # Draw rectangle and name on frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
        cv2.putText(frame, person_name, (x + 5, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        # Prepare attendance entry
        ts = time.time()
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        attendance = [person_name, timestamp]

        # Check if attendance file exists
        exist = os.path.isfile(f"Attendance/Attendance_{date}.csv")

    # Place video frame on background
    try:
        imgBackground[162:162 + frame.shape[0], 55:55 + frame.shape[1]] = frame
    except:
        print("Error: background too small for video placement.")

    cv2.imshow("Attendance System", imgBackground)

    k = cv2.waitKey(1)
    if k == ord('o') and attendance is not None:
        speak(f"Attendance taken for {attendance[0]}")
        time.sleep(1)

        os.makedirs("Attendance", exist_ok=True)
        if exist:
            with open(f"Attendance/Attendance_{date}.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open(f"Attendance/Attendance_{date}.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)

    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
