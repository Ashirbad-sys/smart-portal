from django.db import models
from accounts.models import User


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    company_size = models.CharField(max_length=50, blank=True, choices=[
        ('1-10', '1-10 employees'),
        ('11-50', '11-50 employees'),
        ('51-200', '51-200 employees'),
        ('201-500', '201-500 employees'),
        ('500+', '500+ employees'),
    ])
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} ({self.user.username})"