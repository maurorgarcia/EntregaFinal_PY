from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Perfil


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("avatar", "biografia", "link")
        widgets = {
            "biografia": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
        }

