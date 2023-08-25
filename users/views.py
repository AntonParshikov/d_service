import random
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from users.forms import UsersRegisterForm, UsersForm
from users.models import Users


class UsersListView(LoginRequiredMixin, ListView):
    model = Users

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Users.objects.filter(Q(first_name__icontains=query) | Q(email__icontains=query))
        else:
            return Users.objects.all()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = Users
    template_name = 'users/users_detail.html'
    context_object_name = 'users'


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


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Users
    success_url = reverse_lazy('users:users_list')
    form_class = UsersForm
    permission_required = 'users.change_users'

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    password = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль: {password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )

    request.user.set_password(password)
    request.user.save()
    return redirect(reverse('users:login'))
