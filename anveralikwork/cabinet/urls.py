from django.urls import path
from .views import login, register, profile, logout, profile_edit

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit", profile_edit, name="profile_edit"),
]
