from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #página de login(auth_views.LoginView.as_view(template_name='users/login.html')serve para renderizar o template de login)
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    #página de logout(auth_views.LogoutView.as_view()serve para fazer o logout)
    #path('logout',auth_views.LogoutView.as_view(template_name='users/login.html'),name='logout'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register,name='register'),
]