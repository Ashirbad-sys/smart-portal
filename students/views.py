from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudentProfile
from .forms import StudentProfileForm
from jobs.models import Application


@login_required
def student_dashboard(request):
    try:
        profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        profile = None

    # Application stats
    applications = Application.objects.filter(
        student=profile
    ) if profile else []

    total_applied = len(applications)
    total_shortlisted = sum(1 for a in applications if a.status == 'shortlisted')
    total_pending = sum(1 for a in applications if a.status == 'applied')
    total_selected = sum(1 for a in applications if a.status == 'selected')

    return render(request, 'students/dashboard.html', {
        'profile': profile,
        'total_applied': total_applied,
        'total_shortlisted': total_shortlisted,
        'total_pending': total_pending,
        'total_selected': total_selected,
    })


@login_required
def edit_profile(request):
    try:
        profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'students/edit_profile.html', {'form': form})