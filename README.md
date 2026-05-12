# 🚀 Smart Internship & Placement Portal

A full-stack web application built with Django where students can find internships/jobs and companies can post opportunities.

## 🌟 Live Demo
[Coming soon after deployment]

## 📸 Features

### 👨‍🎓 Students
- Register and create a profile
- Upload resume and profile photo
- Add skills, CGPA, portfolio links
- Browse and search jobs & internships
- Apply with a cover letter
- Track application status in real time
- In-app and email notifications

### 🏢 Companies
- Register and create company profile
- Post jobs and internships
- View and manage applicants
- Update application status
- Email notifications sent automatically

### 🛡️ Admin
- Approve or reject company registrations
- Manage students, companies, jobs
- View platform analytics
- Full Django admin panel access

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite (dev), PostgreSQL (prod) |
| Storage | Django Media Files |
| Email | Gmail SMTP |
| Deployment | Render |

## ⚙️ Local Setup

```bash
# Clone the repo
git clone https://github.com/Ashirbad-sys/smart-portal.git
cd smart-portal

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your values

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## 🔐 Environment Variables

Create a `.env` file with:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 📁 Project Structure

myproject/
├── accounts/        # Custom user model, auth
├── students/        # Student profiles
├── companies/       # Company profiles
├── jobs/            # Jobs, internships, applications
├── core/            # Home, admin dashboard, notifications
├── templates/       # All HTML templates
├── static/          # CSS, JS
├── media/           # User uploads
└── manage.py

## 👨‍💻 Developer

**Ashirbad** — Full Stack Django Developer

## 📄 License
MIT License