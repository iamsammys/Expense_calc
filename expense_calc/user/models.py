"""Module for user moels
Created on 2021-09-26
by Samuel Ezeh
"""
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Custom user manager class
    """

    def create_user(self, email, password=None, **extra_fields):
        """Method to create a user for the project
        Args:
            email (str): The email of the user
            password (str): The password of the user
            **extra_fields: The extra fields to be passed to the user
        
        Returns: The user
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Method to create to manage the creation os a superuser for the project

        Args:
            email (str): The email of the superuser
            password (str): The password of the superuser
            **extra_fields: The extra fields to be passed to the superuser

        Returns: The superuser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        super_user = self.create_user(email, password, **extra_fields)
        return super_user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name