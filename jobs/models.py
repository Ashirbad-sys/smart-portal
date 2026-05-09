from django.db import models
from companies.models import CompanyProfile


class Job(models.Model):

    # Listing Type
    class ListingType(models.TextChoices):
        JOB = 'job', 'Job'
        INTERNSHIP = 'internship', 'Internship'

    # Job Type
    class JobType(models.TextChoices):
        FULL_TIME = 'full_time', 'Full Time'
        PART_TIME = 'part_time', 'Part Time'
        CONTRACT = 'contract', 'Contract'
        REMOTE = 'remote', 'Remote'

    # Application Status
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        CLOSED = 'closed', 'Closed'

    # Core Fields
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='jobs')
    listing_type = models.CharField(max_length=15, choices=ListingType.choices, default=ListingType.JOB)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=15, choices=JobType.choices, default=JobType.FULL_TIME)
    skills_required = models.TextField(help_text="Comma separated e.g. Python, Django, SQL")
    salary = models.CharField(max_length=100, blank=True, help_text="e.g. 5-8 LPA or Negotiable")
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)

    # Internship Only Fields
    stipend = models.CharField(max_length=100, blank=True, help_text="e.g. 10,000/month")
    duration = models.CharField(max_length=100, blank=True, help_text="e.g. 3 months, 6 months")
    is_remote = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company.company_name} ({self.listing_type})"

    @property
    def is_internship(self):
        return self.listing_type == self.ListingType.INTERNSHIP

    @property
    def is_job(self):
        return self.listing_type == self.ListingType.JOB


class Application(models.Model):

    class Status(models.TextChoices):
        APPLIED = 'applied', 'Applied'
        SHORTLISTED = 'shortlisted', 'Shortlisted'
        REJECTED = 'rejected', 'Rejected'
        SELECTED = 'selected', 'Selected'

    student = models.ForeignKey('students.StudentProfile', on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.APPLIED)
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_letter = models.TextField(blank=True, help_text="Optional cover letter")

    class Meta:
        ordering = ['-applied_at']
        unique_together = ['student', 'job']  # prevent duplicate applications

    def __str__(self):
        return f"{self.student.user.username} → {self.job.title} ({self.status})"