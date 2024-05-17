from ..models import User
from ..forms import UserLoginForm, UserRegisterForm
from django.contrib import auth

def login_user(request):
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return True
    return False

def logout_user(request):
    auth.logout(request)
    return True

def register_user(request):
    form = UserRegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        return True
    return False

def profile_edit_data(request):
    user = request.user
    name = request.POST["name"]
    contact_phone_number = request.POST["contact_phone_number"]
    contact_email = request.POST["contact_email"]
    experience = request.POST["experience"]

    user.name = name
    user.contact_phone_number = contact_phone_number
    user.contact_email = contact_email
    user.experience = experience
    user.save()
    return True

def get_user_profile_data(request):
    user_profile_data = {}
    user = request.user
    
    user_profile_data["name"] = user.name
    user_profile_data["contact_phone_number"] = user.contact_phone_number
    user_profile_data["contact_email"] = user.contact_email
    user_profile_data["experience"] = user.experience


    return user_profile_data