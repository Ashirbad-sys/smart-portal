from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CompanyProfile
from .forms import CompanyProfileForm
from jobs.models import Job, Application


@login_required
def company_dashboard(request):
    try:
        profile = request.user.company_profile
    except CompanyProfile.DoesNotExist:
        profile = None

    # Job stats
    if profile:
        total_jobs = Job.objects.filter(company=profile).count()
        open_positions = Job.objects.filter(company=profile, status='open').count()
        total_applicants = Application.objects.filter(job__company=profile).count()
    else:
        total_jobs = 0
        open_positions = 0
        total_applicants = 0

    return render(request, 'companies/dashboard.html', {
        'profile': profile,
        'total_jobs': total_jobs,
        'open_positions': open_positions,
        'total_applicants': total_applicants,
    })

@login_required
def edit_profile(request):
    try:
        profile = request.user.company_profile
    except CompanyProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Company profile updated successfully!')
            return redirect('company_dashboard')
    else:
        form = CompanyProfileForm(instance=profile)

    return render(request, 'companies/edit_profile.html', {'form': form})