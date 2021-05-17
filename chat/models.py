from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    custom_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    date = models.CharField(default=custom_date,max_length=60)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)
    
    def __str__(self):
        return f"User:{self.user} Message:{self.value}"
