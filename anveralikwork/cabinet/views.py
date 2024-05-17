from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from .services.services import login_user, logout_user, register_user, profile_edit_data, get_user_profile_data
from django.contrib.auth.decorators import login_required

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

@login_required
def logout(request):
    logout_user(request)
    return redirect("index")

@login_required
def profile(request):
    return render(request, "cabinet/cabinet_profile.html")

@login_required
def profile_edit(request):
    data = {}
    if request.method == "POST":
        profile_edit_data(request)
        return redirect("profile")
    else:
        user_profile_data = get_user_profile_data(request)
        form = UserProfileForm(initial=user_profile_data)

    data["form"] = form
    return render(request, "cabinet/cabinet_profile_edit.html", data)