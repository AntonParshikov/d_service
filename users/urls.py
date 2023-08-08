from django.urls import path

from users.apps import UsersConfig
from users.views import UsersListView, UserDetailView, UsersCreateView, IndexListView, UsersUpdateView, UsersDeleteView, \
    LoginView, LogoutView, RegisterView, UserUpdateView, generate_password

app_name = UsersConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('create/', UsersCreateView.as_view(), name='create_user'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='users_confirm_delete'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_password, name='generate_password'),

]
