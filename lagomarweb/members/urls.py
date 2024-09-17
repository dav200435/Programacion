from django.urls import path

from . import  views

urlpatterns = [
    path("members/", views.members, name="members"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
]