from django import forms
from .models import CompanyProfile


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ['user', 'is_approved', 'created_at', 'updated_at']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact number'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Software, Finance'}),
            'company_size': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City, State'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'About your company'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }