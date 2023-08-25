from django.urls import path
from django.views.decorators.cache import cache_page

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_password, UsersListView, \
    UserDetailView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_password, name='generate_password'),

]
