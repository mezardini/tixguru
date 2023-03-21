from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Event(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField()
    description = models.TextField()
    tix_price = models.FloatField()
    creator = models.ForeignKey(User, related_name='uservent', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tix_code = models.CharField(max_length=30)
    tix_mail = models.EmailField()
    tix_name = models.CharField(max_length=300)

    def __str__(self):
        return self.tix_name

class Bookmark(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    creator = models.CharField(max_length=200)