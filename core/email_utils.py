from django.core.mail import send_mail
from django.conf import settings


def send_application_status_email(student_user, job, status):
    subject_map = {
        'shortlisted': f'You have been Shortlisted for {job.title}!',
        'selected': f'Congratulations! You are Selected for {job.title}!',
        'rejected': f'Application Update for {job.title}',
        'applied': f'Application Received for {job.title}',
    }

    message_map = {
        'shortlisted': f"""
Hi {student_user.username},

Great news! You have been shortlisted for the position of {job.title} at {job.company.company_name}.

The company will be in touch with you soon for the next steps.

Best of luck!
Smart Portal Team
        """,
        'selected': f"""
Hi {student_user.username},

Congratulations! 🎉

You have been selected for the position of {job.title} at {job.company.company_name}.

The company will contact you shortly with further details.

Well done!
Smart Portal Team
        """,
        'rejected': f"""
Hi {student_user.username},

Thank you for applying for {job.title} at {job.company.company_name}.

Unfortunately, your application was not successful this time. Don't be discouraged — keep applying!

Best wishes,
Smart Portal Team
        """,
        'applied': f"""
Hi {student_user.username},

Your application for {job.title} at {job.company.company_name} has been received successfully.

You can track your application status on Smart Portal.

Good luck!
Smart Portal Team
        """,
    }

    subject = subject_map.get(status, 'Application Status Update')
    message = message_map.get(status, 'Your application status has been updated.')

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[student_user.email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Email sending failed: {e}")


def send_company_approval_email(company):
    subject = f'Your Company {company.company_name} has been Approved!'
    message = f"""
Hi {company.user.username},

Great news! Your company {company.company_name} has been approved on Smart Portal.

You can now:
- Post jobs and internships
- View applicants
- Manage your listings

Login now and get started!

Smart Portal Team
    """

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[company.user.email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Email sending failed: {e}")