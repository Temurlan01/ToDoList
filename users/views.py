from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import  redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class UserRegistrationView(TemplateView):
    """
    вьюшка для того что бы показывать страницу лоя регистрации
    """
    template_name = 'register.html'


class MakeUserRegistrationView(View):
    """
    вьюшка для того чтобы регистрировать пользователя
    """

    def post(self, request, *args, **kwargs):
        data = request.POST
        password1 = data['password1']
        password2 = data['password2']

        if password1 != password2:
            messages.error(request, "Пароли не совпадают.")
            return redirect('register-url')

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует.")
            return redirect('register-url')

        user = CustomUser.objects.create_user(
            email=email, password1=password1,
            first_name=first_name, last_name=last_name
        )

        login(request, user)

        return redirect('home-url')


class LoginListView(TemplateView):
    """
    вьюшка для показа страницы для логина
    """
    template_name = 'Login.html'


class MakeLoginView(View):
    """
    вьюшка для того что бы пользователь мог входить в акк
    """
    def post(self, request,):
        data = request.POST
        email = data['email']
        password = data['password']

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.error(request, "пользователь не найден.")
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('home-url')

        messages.error(request, "Неверный пароль.")
        return redirect('login-url')


class MakeLogoutView(View):
    """
    вьюшка для выхода из акк
    """
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login-url')