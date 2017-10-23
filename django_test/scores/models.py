from django.db import models
from django.urls import reverse

# Create your models here.
class Session(models.Model):
    homeTeam = models.CharField(max_length=100);
    awayTeam = models.CharField(max_length=100);

class Chat(models.Model):
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)
    chat = models.CharField(max_length=100);
