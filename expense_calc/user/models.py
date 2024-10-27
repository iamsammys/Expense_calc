from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from shared.basemodel import Basemodel


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
            first_name (str): The first name of the user
            last_name (str): The last name of the user
            username (str): The username of the user

        Returns: The user
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Method to manage the creation of a superuser for the project

        Args:
            email (str): The email of the superuser
            password (str): The password of the superuser
            **extra_fields: The extra fields to be passed to the superuser
            first_name (str): The first name of the superuser
            last_name (str): The last name of the superuser
            username (str): The username of the superuser

        Returns: The superuser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(
            email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, Basemodel):
    """
    Custom user model
    """
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """Method to return the string representation of the object

        Returns:
            The string representation of the object
        """
        return "[{}].({}) {}".format(self.__class__.__name__, self.id, self.email)
