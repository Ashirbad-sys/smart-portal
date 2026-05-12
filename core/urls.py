from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    # Notifications
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<int:pk>/read/', views.mark_notification_read, name='mark_notification_read'),

    # Admin
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage/companies/', views.manage_companies, name='manage_companies'),
    path('manage/companies/<int:pk>/approve/', views.approve_company, name='approve_company'),
    path('manage/companies/<int:pk>/reject/', views.reject_company, name='reject_company'),
    path('manage/students/', views.manage_students, name='manage_students'),
    path('manage/jobs/', views.manage_jobs, name='manage_jobs'),
    path('manage/jobs/<int:pk>/delete/', views.delete_job_admin, name='delete_job_admin'),
    path('manage/users/<int:pk>/delete/', views.delete_user, name='delete_user'),
]