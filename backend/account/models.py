import uuid
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Profile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
