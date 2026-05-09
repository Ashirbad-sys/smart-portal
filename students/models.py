from django.db import models
from accounts.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    college = models.CharField(max_length=200, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    skills = models.TextField(blank=True, help_text="Comma separated e.g. Python, Django, SQL")
    portfolio_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"