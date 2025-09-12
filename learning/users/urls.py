from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    #página de login(auth_views.LoginView.as_view(template_name='users/login.html')serve para renderizar o template de login)
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
]