from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import register_view, UserDetailView, UserUpdateView, UserChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('registration/', register_view, name='regis'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/', UserUpdateView.as_view(), name='user-update-profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password'),
]