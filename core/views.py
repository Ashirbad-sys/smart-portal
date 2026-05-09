from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import User
from students.models import StudentProfile
from companies.models import CompanyProfile
from jobs.models import Job, Application


def home_view(request):
    return render(request, 'core/home.html')


# ── Admin Views ──

def admin_only(view_func):
    """Custom decorator to restrict access to admin users only."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_admin_user:
            messages.error(request, 'You are not authorized to view this page.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


@admin_only
def admin_dashboard(request):
    total_students = StudentProfile.objects.count()
    total_companies = CompanyProfile.objects.count()
    total_jobs = Job.objects.filter(listing_type='job').count()
    total_internships = Job.objects.filter(listing_type='internship').count()
    total_applications = Application.objects.count()
    pending_companies = CompanyProfile.objects.filter(is_approved=False).count()

    recent_applications = Application.objects.select_related(
        'student', 'job', 'job__company'
    ).order_by('-applied_at')[:5]

    return render(request, 'core/admin_dashboard.html', {
        'total_students': total_students,
        'total_companies': total_companies,
        'total_jobs': total_jobs,
        'total_internships': total_internships,
        'total_applications': total_applications,
        'pending_companies': pending_companies,
        'recent_applications': recent_applications,
    })


@admin_only
def manage_companies(request):
    companies = CompanyProfile.objects.select_related('user').all()
    return render(request, 'core/manage_companies.html', {'companies': companies})


@admin_only
def approve_company(request, pk):
    company = get_object_or_404(CompanyProfile, pk=pk)
    company.is_approved = True
    company.save()
    messages.success(request, f'{company.company_name} has been approved!')
    return redirect('manage_companies')


@admin_only
def reject_company(request, pk):
    company = get_object_or_404(CompanyProfile, pk=pk)
    company.is_approved = False
    company.save()
    messages.warning(request, f'{company.company_name} has been rejected!')
    return redirect('manage_companies')


@admin_only
def manage_students(request):
    students = StudentProfile.objects.select_related('user').all()
    return render(request, 'core/manage_students.html', {'students': students})


@admin_only
def manage_jobs(request):
    jobs = Job.objects.select_related('company').all()
    return render(request, 'core/manage_jobs.html', {'jobs': jobs})


@admin_only
def delete_job_admin(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
    return redirect('manage_jobs')


@admin_only
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
    return redirect('manage_students')