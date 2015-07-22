# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm, SignupForm
from django.views.generic import View
from django.contrib.auth.models import User


class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next',
                                          'blogs_home')  # si no existe el parámetro GET 'next', le mandamos a 'photos_home'
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)



class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('blogs_home')



class SignupView(View):

    def get(self, request):
        """
        Muestra formulario para registrarse
        """
        form = SignupForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'users/signup.html', context)


    def post(self, request):
        """
        Registra a un usario con la información de POST
        """
        form = SignupForm(request.POST)
        if form.is_valid():

            success_message = ''
            error_message = ''
            possible_user = User.objects.filter(username=form.cleaned_data.get('usr'))
            if len(possible_user) > 0:
                error_message = u'El nombre de usuario ya está siendo usado. Por favor elija otro'
            else:
                new_user = User()
                new_user.username = form.cleaned_data.get('usr')
                new_user.first_name = form.cleaned_data.get('fst_name')
                new_user.last_name = form.cleaned_data.get('lst_name')
                new_user.email = form.cleaned_data.get('email')
                new_user.password = make_password(form.cleaned_data.get('pwd'))
                new_user.save()

                form = SignupForm() # reiniciamos el formulario
                success_message = u'Usuario ' + new_user.username + u' registrado con éxito! '
                success_message += u'<a href="{0}">'.format(
                    reverse(u'users_login', args=[])
                )
                success_message += u'Entrar'
                success_message += u'</a>'

            context = {
                'form': form,
                'success_message': success_message,
                'error_message': error_message
            }
            return render(request, 'users/signup.html', context)
















