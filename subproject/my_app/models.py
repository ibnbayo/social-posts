from datetime import datetime
from time import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50) #input
    body = models.TextField() #large input
    date_created = models.DateTimeField(default=timezone.now) #calendar
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #one to many is foreign key, many to many also exists

