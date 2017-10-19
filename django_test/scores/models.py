from django.db import models
from django.urls import reverse

# Create your models here.
class Session(models.Model):
    homeTeam = models.CharField(max_length=100);
    awayTeam = models.CharField(max_length=100);

import uuid

class SessionInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)
