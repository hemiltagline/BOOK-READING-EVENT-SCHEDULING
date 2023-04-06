from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")

        # Check if user with same email and user_type exists
        user_type = extra_fields.get("user_type")
        if User.objects.filter(email=email, user_type=user_type).exists():
            raise ValueError("User with same email and user_type already exists.")

        extra_fields["password"] = make_password(password)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    ORGANIZER = "ORGANIZER"
    CUSTOMER = "CUSTOMER"

    USER_TYPE = [
        (ORGANIZER, "ORGANIZER"),
        (CUSTOMER, "CUSTOMER"),
    ]
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(
        verbose_name="Phone no.",
        help_text="Provide a number with country code (e.g. +12125552368).",
    )
    address = models.CharField(max_length=200, null=True, blank=True)
    user_type = MultiSelectField(max_length=10, choices=USER_TYPE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name
