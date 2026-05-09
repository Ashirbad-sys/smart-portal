from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def company_dashboard(request):
    return render(request, 'companies/dashboard.html')