
# 🚗 Old Car Price Prediction System (Django + ML)

A full-stack web application built with **Django** and **Machine Learning** to predict the resale price of used cars based on various features.

🔗 **Live Demo:**  
https://srikumarpal.pythonanywhere.com/

---

## 📌 Features

- 🔮 Machine Learning based price prediction
- 🌗 Light / Dark mode UI
- ⏳ Loading spinner during prediction
- 📊 Animated prediction result
- 🧠 Session-based prediction history (last 5)
- 🔐 User Authentication (Login / Signup)
- 🛠 Admin dashboard support
- 📱 Fully responsive UI (Bootstrap 5)

---

## 🧰 Tech Stack

**Frontend**
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

**Backend**
- Python
- Django 5

**Machine Learning**
- Scikit-learn
- Pickle model

**Database**
- SQLite3

**Deployment**
- PythonAnywhere

------------------------------------------------------------------------------------------

## 📂 Project Structure
oldcar/
│── manage.py
│── model.pkl
│── db.sqlite3
│
├── oldcar/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── predictor/
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ ├── index.html
│ │ ├── result.html
│ │ └── registration/
│ │ ├── login.html
│ │ └── signup.html
│ └── static/
│ └── style.css

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/srikumar-pal/old-car-price-prediction-django.git
cd old-car-price-prediction-django
Create Virtual Environment
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Migrations
python manage.py migrate

5️⃣ Start Server
python manage.py runserver


Open browser:
👉 http://127.0.0.1:8000/
🔐 Authentication URLs

Login → /accounts/login/

Logout → /accounts/logout/

Signup → /signup/
------------------------------------------------------------------------------------------
