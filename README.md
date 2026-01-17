
# Face Recognition Based Smart Attendance System with Web Apps Using Machine Learning

## Overview
The **Face Recognition Based Smart Attendance System** is an intelligent solution that automates attendance marking using facial recognition technology. By leveraging **machine learning**, it accurately identifies individuals in real-time and updates attendance records automatically. The system also features a **web application** for managing and monitoring attendance efficiently.

---

## Features
- **Automated Attendance:** Real-time face recognition for automatic attendance marking.
- **Web Dashboard:** Interactive dashboard to view and manage attendance records.
- **Secure Authentication:** Access control for students, teachers, and administrators.
- **Reports & Analytics:** Generate daily, weekly, and monthly attendance reports.
- **Multi-user Support:** Handles multiple classes and sessions simultaneously.
- **High Accuracy:** Uses advanced machine learning models for reliable face detection.

---

## Technologies Used
- **Backend:** Python, Flask / Django  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap / React  
- **Machine Learning:** OpenCV, face_recognition library, NumPy  
- **Database:** MySQL / SQLite / MongoDB  
- **Deployment:** Local server / Cloud platform  

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd <your-project-folder>
````

### 2. Create Virtual Environment

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

* Configure the database connection in `config.py` or `settings.py`.
* Run migrations or scripts to create necessary tables.

### 5. Run the Application

```bash
python app.py   # or flask run / python manage.py runserver
```

* Access the web app at `http://localhost:5000`.

---

## Usage

1. Register students and faculty in the system.
2. Capture or upload images for facial recognition registration.
3. Start an attendance session; the system will automatically recognize faces.
4. Monitor and export attendance reports from the web dashboard.

---

## Folder Structure

```
Face-Recognition-Attendance-System/
│
├── app.py / manage.py        # Main application
├── requirements.txt          # Python dependencies
├── templates/                # HTML templates
├── static/                   # CSS, JS, and images
├── database/                 # Database files or scripts
├── face_recognition/         # ML models and scripts
└── README.md                 # Project documentation
```

---

## Future Enhancements

* SMS/Email notifications for absentees.
* Multi-classroom and multi-location support.
* Mobile/web hybrid platform integration.
* Real-time alerts for unrecognized faces.

---

## Contributors

* **Kommati Sruthi** – Development, ML Model, Web App Integration


---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

```

---

If you want, I can also make a **GitHub-ready version with badges, GIF demo placeholders, and clickable links**, which will make your project look **very professional on your portfolio**.  

Do you want me to do that next?
```
