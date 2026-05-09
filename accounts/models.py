from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    class Role(models.TextChoices):
        STUDENT = 'student', 'Student'
        COMPANY = 'company', 'Company'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )

    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_student(self):
        return self.role == self.Role.STUDENT

    @property
    def is_company(self):
        return self.role == self.Role.COMPANY

    @property
    def is_admin_user(self):
        return self.role == self.Role.ADMIN