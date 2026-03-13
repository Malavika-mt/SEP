from django import forms
from .models import Student_Register


class Student_RegisterForm(forms.ModelForm):
    
    class Meta:
        model = Student_Register
        fields = ["first_name", "last_name", "email", "department"]

    widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}),
        'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}),
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
        'department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your department'}),

    }

def clean_email(self):
    email=self.cleaned_data.get('email')
    if not email.endswith('@cce.edu.in'):
        raise forms.ValidationError("Email must be from the domain cce.edu.in")
    return email




