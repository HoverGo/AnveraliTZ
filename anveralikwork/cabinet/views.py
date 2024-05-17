from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from .services.services import login_user, logout_user, register_user

def register(request):
    data = {}
    form = UserRegisterForm()

    if request.method == "POST":
        print(request.POST)
        if register_user(request):
            return redirect("index")
        else:
            data["form_error"] = "invalid data"
        
    
    data["form"] = form
    return render(request, "cabinet/cabinet_register.html", data)


def login(request):
    data = {}
    if request.method == "POST":
        if login_user(request):
            return redirect("index")
        else:
            form = UserLoginForm()
            data["form_error"] = "invalid data"
    else:
        form = UserLoginForm()

    data["form"] = form

    return render(request, "cabinet/cabinet_login.html", data)

def logout(request):
    logout_user(request)
    return redirect("index")

def profile(request):
    return render(request, "cabinet/cabinet_profile.html")