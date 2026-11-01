# 🚀 Smart Internship & Placement Portal

A full-stack Django web application where students find internships and jobs, companies post opportunities, and admins moderate the platform.

## 🌟 Live Demo
**https://smart-portal-z5md.onrender.com**

> Hosted on Render's free tier, so the first load may take 30-50 seconds while the server wakes up.

**Try it with demo accounts:**

| Role | Username | Password |
|---|---|---|
| Student | `demo_student` | `your-demo-password` |
| Company | `demo_company` | `your-demo-password` |

## 📸 Screenshots
<!-- Add 3-4 screenshots: home page, job listing, student dashboard, admin dashboard -->

## ✨ Features

### 👨‍🎓 Students
- Register, log in, and build a profile (skills, CGPA, portfolio links)
- Upload a resume and profile photo
- Browse and search jobs and internships with filters
- Apply with an optional cover letter
- Track application status: Applied, Shortlisted, Rejected, Selected
- In-app notifications for status changes

### 🏢 Companies
- Register and create a company profile
- Post, edit, and delete jobs and internships
- View applicants and update their status

### 🛡️ Admin
- Approve or revoke company registrations
- Manage students, companies, and listings
- View platform analytics (users, jobs, applications)

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite (local), Neon PostgreSQL (production) |
| File storage | Cloudinary (resumes, photos, logos) |
| Email | Gmail SMTP (works locally; blocked on Render's free tier) |
| Deployment | Render, WhiteNoise, Gunicorn |

## ⚙️ Local Setup

```bash
git clone https://github.com/Ashirbad-sys/smart-portal.git
cd smart-portal

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

Create a `.env` file in the project root (see below), then:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

After creating a superuser, open `/admin/`, edit your user, and set **Role** to **Admin** so the custom admin dashboard (`/admin-dashboard/`) works.

## 🔐 Environment Variables

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Cloudinary (media uploads)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Production (`DEBUG=False`) also requires `DATABASE_URL` pointing to a PostgreSQL database.

## 📁 Project Structure

```
smart-portal/
├── accounts/        # Custom user model, authentication
├── students/        # Student profiles
├── companies/       # Company profiles
├── jobs/            # Jobs, internships, applications
├── core/            # Home, admin dashboard, notifications
├── smart_portal/    # Project settings and URLs
├── templates/       # HTML templates
├── static/          # CSS
└── manage.py
```

## 📝 Notes
- Resume links are public Cloudinary URLs. Private, signed URLs would be the next step for real student data.
- Email alerts are skipped on the live site because the free hosting tier blocks SMTP.

## 👨‍💻 Developer
**Ashirbad Pattanayak**