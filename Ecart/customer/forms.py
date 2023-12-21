from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))
    password = forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control"})))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control"})))
    password2 = forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control"})))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        widgets ={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }
        
class CartForm(forms.Form):
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))