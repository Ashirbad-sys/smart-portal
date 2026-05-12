from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application
from .forms import JobForm, ApplicationForm


# ── Public Views ──

def job_list(request):
    jobs = Job.objects.filter(listing_type='job', status='open')
    query = request.GET.get('q')
    location = request.GET.get('location')
    job_type = request.GET.get('job_type')

    if query:
        jobs = jobs.filter(title__icontains=query) | jobs.filter(skills_required__icontains=query)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    return render(request, 'jobs/job_list.html', {
        'jobs': jobs,
        'query': query,
        'location': location,
        'job_type': job_type,
        'listing_type': 'job'
    })


def internship_list(request):
    internships = Job.objects.filter(listing_type='internship', status='open')
    query = request.GET.get('q')
    location = request.GET.get('location')
    is_remote = request.GET.get('is_remote')

    if query:
        internships = internships.filter(title__icontains=query) | internships.filter(skills_required__icontains=query)
    if location:
        internships = internships.filter(location__icontains=location)
    if is_remote:
        internships = internships.filter(is_remote=True)

    return render(request, 'jobs/internship_list.html', {
        'internships': internships,
        'query': query,
        'location': location,
        'is_remote': is_remote,
        'listing_type': 'internship'
    })


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, listing_type='job')
    has_applied = False
    if request.user.is_authenticated and hasattr(request.user, 'student_profile'):
        has_applied = Application.objects.filter(
            student=request.user.student_profile, job=job
        ).exists()
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'has_applied': has_applied
    })


def internship_detail(request, pk):
    internship = get_object_or_404(Job, pk=pk, listing_type='internship')
    has_applied = False
    if request.user.is_authenticated and hasattr(request.user, 'student_profile'):
        has_applied = Application.objects.filter(
            student=request.user.student_profile, job=internship
        ).exists()
    return render(request, 'jobs/internship_detail.html', {
        'internship': internship,
        'has_applied': has_applied
    })


# ── Student Views ──

@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    if not hasattr(request.user, 'student_profile'):
        messages.error(request, 'Only students can apply for jobs.')
        return redirect('job_list')

    if Application.objects.filter(student=request.user.student_profile, job=job).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student_profile
            application.job = job
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('my_applications')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply.html', {'form': form, 'job': job})


@login_required
def my_applications(request):
    if not hasattr(request.user, 'student_profile'):
        messages.error(request, 'Only students can view applications.')
        return redirect('home')

    applications = Application.objects.filter(
        student=request.user.student_profile
    ).select_related('job', 'job__company')

    return render(request, 'jobs/my_applications.html', {'applications': applications})


# ── Company Views ──

@login_required
def post_job(request, listing_type='job'):
    if not hasattr(request.user, 'company_profile'):
        messages.error(request, 'Only companies can post jobs.')
        return redirect('home')

    if not request.user.company_profile.is_approved:
        messages.warning(request, 'Your company profile is pending approval. You cannot post jobs yet.')
        return redirect('company_dashboard')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.company_profile
            job.listing_type = listing_type
            job.save()
            messages.success(request, f'{"Internship" if listing_type == "internship" else "Job"} posted successfully!')
            return redirect('my_postings')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {
        'form': form,
        'listing_type': listing_type
    })


@login_required
def my_postings(request):
    if not hasattr(request.user, 'company_profile'):
        messages.error(request, 'Only companies can view postings.')
        return redirect('home')

    jobs = Job.objects.filter(company=request.user.company_profile)
    return render(request, 'jobs/my_postings.html', {'jobs': jobs})


@login_required
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk, company=request.user.company_profile)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('my_postings')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/post_job.html', {
        'form': form,
        'listing_type': job.listing_type,
        'edit': True
    })


@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk, company=request.user.company_profile)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
    return redirect('my_postings')


@login_required
def view_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk, company=request.user.company_profile)
    applications = Application.objects.filter(job=job).select_related('student', 'student__user')
    return render(request, 'jobs/applicants.html', {
        'job': job,
        'applications': applications
    })


@login_required
def update_application_status(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if not hasattr(request.user, 'company_profile'):
        messages.error(request, 'Unauthorized.')
        return redirect('home')

    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['applied', 'shortlisted', 'rejected', 'selected']:
            application.status = status
            application.save()

            # In-app notification
            from core.models import Notification
            status_messages = {
                'shortlisted': f'🌟 You have been shortlisted for {application.job.title} at {application.job.company.company_name}!',
                'selected': f'🎉 Congratulations! You have been selected for {application.job.title} at {application.job.company.company_name}!',
                'rejected': f'Your application for {application.job.title} at {application.job.company.company_name} was not successful this time.',
                'applied': f'Your application for {application.job.title} has been received.',
            }
            Notification.objects.create(
                user=application.student.user,
                message=status_messages.get(status, 'Your application status has been updated.')
            )

            # Email notification
            from core.email_utils import send_application_status_email
            send_application_status_email(
                student_user=application.student.user,
                job=application.job,
                status=status
            )

            messages.success(request, 'Application status updated and student notified!')

    return redirect('view_applicants', pk=application.job.pk)