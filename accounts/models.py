from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    REQUIRED_FIELDS = ["first_name", "last_name"]
