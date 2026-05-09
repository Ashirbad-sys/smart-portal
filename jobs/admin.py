from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'listing_type', 'job_type', 'location', 'status', 'deadline', 'created_at')
    list_filter = ('listing_type', 'job_type', 'status')
    search_fields = ('title', 'company__company_name', 'location')
    list_editable = ('status',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'job', 'status', 'applied_at')
    list_filter = ('status',)
    search_fields = ('student__user__username', 'job__title')
    list_editable = ('status',)