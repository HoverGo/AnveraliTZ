from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Write username",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Write password",
    }))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Write username",
    }))
        
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Write password",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Repeat password",
        }))
    
    user_role = forms.ChoiceField(choices=[('customer', 'Customer'), ('executor', 'Executor')], widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "user_role")

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user_role = self.cleaned_data.get('user_role')
        if user_role == 'executor':
            user.is_executor = True
        elif user_role == 'customer':
            user.is_customer = True
        
        if commit:
            user.save()
        return user