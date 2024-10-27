"""Base module for classes that need to be shared across the project.

Created by: Samuel Ezeh
Created on: 2021-10-25
"""
from django.db import models
from uuid import uuid4
from datetime import datetime
from django.db.models import UUIDField
from django.utils import timezone


class Basemodel(models.Model):
    """Base class for classes that need to be shared across the project.
    """
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __init__(self, *args, **kwargs):
        """Constructor for the Basemodel class

        Args:
            *args: The positional arguments to be passed to the method
            **kwargs: The keyword arguments to be passed to the method
        """
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = str(uuid4())
        if not self.created_at:
            self.created_at = str(timezone.now())
        if not self.updated_at:
            self.updated_at = str(timezone.now())

    def save(self, *args, **kwargs):
        """Method to save the object to the database

        Args:
            *args: The positional arguments to be passed to the method
            **kwargs: The keyword arguments to be passed to the method
        """
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
