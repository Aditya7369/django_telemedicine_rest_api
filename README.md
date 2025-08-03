# django_telemedicine_rest_api
---
▰ Django Backend Project : Telemedicine backend service

▰ Backend Developer Practical Assignment
This assignment is designed to evaluate your practical backend development skills.
You will be expected to build, secure and document a simple API-based service using the following technologies and practices.

▰ Assignment Scenario
Build a simplified Telemedicine backend service with the following features:

▰ Functional Requirements
* User Registration and Login with JWT authentication
* Doctor and Patient roles with basic CRUD
* Appointment creation and listing per user
* WebSocket or polling endpoint to simulate real-time status update for a doctor (online/offline)
* Swagger UI or Postman collection for all endpoints

▰ Database Schema (Example)
* Users: id, name, email, password_hash, role
* Appointments: id, patient_id, doctor_id, status, timestamp

---

# Project Setup Instructions :

* git clone https://github.com/Aditya7369/django_telemedicine_rest_api.git
* cd dp_telemedicine

* python -m venv env
* source env/bin/activate      # Linux/Mac
* env\Scripts\activate         # Windows

* pip install -r requirements.txt
* python manage.py runserver

---



