from django import forms
from .models import Job, Application


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['company', 'listing_type', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Backend Developer'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe the role...'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Bangalore, India'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'skills_required': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, SQL'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 5-8 LPA'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'stipend': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10,000/month'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 3 months'}),
            'is_remote': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Tell the company why you are a good fit (optional)...'
            }),
        }