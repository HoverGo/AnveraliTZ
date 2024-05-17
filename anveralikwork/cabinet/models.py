from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, username, password, executor, customer):
        if username is None:
            raise TypeError("Users must have a username")
        
        if password is None:
            raise TypeError("Users must have a password")
        
        if executor is None or customer is None:
            raise TypeError("Users must have a role")
        
        user = self.model(username=username)
        user.set_password(password)

        if executor == True and customer == True:
            user.is_executor = True
            user.is_customer = True
        elif executor == True:
            user.is_executor = True
        elif customer == True:
            user.is_customer = True
        user.save()

        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username, password, True, True)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9][a-zA-Z0-9_]*$",
                message=("Invalid username"),
                code="invalid_username",
            ),
        ],
    )

    password = models.CharField(
        max_length=256,
        validators=[
            RegexValidator(
                regex=r"^[A-Za-z\d!@#$%^&*()_+]+$",
                message=("Invalid password"),
                code="invalid_password",
            ),
        ],
    )

    name = models.CharField(max_length=25, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex=r'^\+\d{1,3} \(\d{3}\) \d{3}-\d{4}$', message='Invalid phone number')], null=True, blank=True)
    experience = models.CharField(null=True, blank=True)

    is_executor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
