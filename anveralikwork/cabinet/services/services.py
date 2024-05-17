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