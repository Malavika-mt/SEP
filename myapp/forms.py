from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Student_RegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}))

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('@cce.edu.in'):
            raise forms.ValidationError("Email must be from the domain cce.edu.in")
        return email




