from django.shortcuts import render


def register(request):
    return render(request, "cabinet/cabinet_register.html")


def login(request):
    return render(request, "cabinet/cabinet_login.html")

def profile(request):
    return render(request, "cabinet/cabinet_profile.html")