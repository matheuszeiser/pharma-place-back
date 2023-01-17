import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id: models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    name: models.CharField(max_length=50)
    email: models.EmailField(unique=True)
    photo: models.URLField()
    isPharmacy: models.BooleanField(default=False)
    address: models.CharField(max_length=100)
    city: models.CharField(max_length=50)
    state: models.CharField(max_length=50)

    REQUIRED_FIELDS = ["name", "email"]
