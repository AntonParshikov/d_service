import secrets
import string

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UsersRegisterForm, UsersForm
from users.models import Users


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = Users
    form_class = UsersRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Добро пожаловать на наш сайт!',
            message='Поздравляем с регистрацией на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = Users
    success_url = reverse_lazy('users:profile')
    form_class = UsersForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(16))  # генерируем пароль длиной 16 символов
    request.user.set_password(password)
    request.user.save()

    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {password}!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    return redirect(reverse('users:login'))
