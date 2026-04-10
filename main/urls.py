from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "main"

urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("perfil/", views.perfil, name="perfil"),
    path("editar-perfil/", views.editar_perfil, name="editar_perfil"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="main:index"), name="logout"),
]