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
    

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'contact_phone_number', 'contact_email', 'experience')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your name'}),
            'contact_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7(XXX)XXX-XXXX', "pattern": "\+7\d{10}", "title": "Phone number must be in the format '+79993211432'"}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write your email'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your experience'}),
        }