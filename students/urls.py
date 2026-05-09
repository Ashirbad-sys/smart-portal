from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_student_profile'),
]