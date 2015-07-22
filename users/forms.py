# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):

    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(forms.Form):

    """
    Formulario para el registro de usuarios
    """
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    fst_name = forms.CharField(label="Nombre")
    lst_name = forms.CharField(label="Apellidos")
    email = forms.EmailField(label="E-mail")