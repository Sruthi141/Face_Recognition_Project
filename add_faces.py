import cv2
import pickle
import numpy as np
import os

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i = 0
name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))
        if i % 10 == 0:
            faces_data.append(resized_img)
        i += 1
        cv2.putText(frame, str(len(faces_data)), (50, 50),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) >= 100:
        break

video.release()
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(len(faces_data), -1)

# Update names
names_path = 'data/names.pkl'
faces_path = 'data/faces_data.pkl'

if os.path.exists(names_path):
    with open(names_path, 'rb') as f:
        names = pickle.load(f)
    names = names + [name]*len(faces_data)
else:
    names = [name]*len(faces_data)
with open(names_path, 'wb') as f:
    pickle.dump(names, f)

# Update faces
if os.path.exists(faces_path):
    with open(faces_path, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
else:
    faces = faces_data
with open(faces_path, 'wb') as f:
    pickle.dump(faces, f)

print(f"Added {len(faces_data)} face images for {name}")
