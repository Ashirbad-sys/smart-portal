from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import StudentProfile
from .forms import StudentProfileForm


@login_required
def student_dashboard(request):
    try:
        profile = request.user.student_profile
    except StudentProfile.DoesNotExist:
        profile = None
    return render(request, 'students/dashboard.html', {'profile': profile})


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