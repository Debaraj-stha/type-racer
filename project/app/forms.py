from django import forms
from .models import Customuser
class LoginForm(forms.Form):
    phone = forms.CharField(label="Phone",max_length=13,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    password = forms.CharField(label="Password",max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class SignupForm(forms.Form):
    class Meta:
        model=Customuser
        fields=('phone','firstname', 'lastname', 'password')
    widgets={
        "phone": forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class': 'form-control','type':'tel'})),
        "firstname": forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class': 'form-control'})),
        "lastname": forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class': 'form-control'})),
        "password": forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        }