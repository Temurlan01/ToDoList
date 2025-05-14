from urllib import request
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class UserRegistrationView(TemplateView):
    template_name = 'register.html'


class MakeUserRegistrationView(View):

    def post(self, request):
        data = request.POST

        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:

            first_name = data['firstName']
            last_name = data['lastName']
            email = data['email']
            user = CustomUser.objects.create_user(
                email=email, password1=password1,
                first_name=first_name, last_name=last_name,
            )
            return redirect('home-url')
        else:
            return HttpResponse('Вы  не правильно ввели пароль')


class LoginListView(TemplateView):
    template_name = 'Login.html'


class MakeLoginView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data['email']
        password = data['password']

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return HttpResponse('Такой электронной почты не существует')



        correct = user.check_password(password)

        if correct == True:
            login(request, user)
            return redirect('home-url')
        else:
            return HttpResponse('Вы не правильно ввели пароль')

class MakeLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login-url')