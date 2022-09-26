
from django.urls import path
from .views import UserRegistrationView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # path('',views.home, name = "home")
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name = 'registration/change_password.html')),
    path('password_success', views.password_success, name= "password_success")
    
    
]