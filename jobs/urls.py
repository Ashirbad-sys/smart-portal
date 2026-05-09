from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.job_list, name='job_list'),
    path('internships/', views.internship_list, name='internship_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('internships/<int:pk>/', views.internship_detail, name='internship_detail'),

    # Student
    path('<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),

    # Company
    path('post/job/', views.post_job, {'listing_type': 'job'}, name='post_job'),
    path('post/internship/', views.post_job, {'listing_type': 'internship'}, name='post_internship'),
    path('my-postings/', views.my_postings, name='my_postings'),
    path('<int:pk>/edit/', views.edit_job, name='edit_job'),
    path('<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('<int:pk>/applicants/', views.view_applicants, name='view_applicants'),
    path('application/<int:pk>/update-status/', views.update_application_status, name='update_application_status'),
]