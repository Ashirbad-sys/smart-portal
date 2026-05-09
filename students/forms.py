from django import forms
from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user', 'created_at', 'updated_at']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your college name'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. B.Tech'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Computer Science'}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 8.5'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, SQL'}),
            'portfolio_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us about yourself'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}),
        }