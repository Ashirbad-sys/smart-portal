from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CompanyProfile
from .forms import CompanyProfileForm


@login_required
def company_dashboard(request):
    try:
        profile = request.user.company_profile
    except CompanyProfile.DoesNotExist:
        profile = None
    return render(request, 'companies/dashboard.html', {'profile': profile})


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