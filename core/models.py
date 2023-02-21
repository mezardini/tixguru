from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify  
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Organizer(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    biz_name = models.CharField(max_length=1000,null=True)
    slug = models.SlugField(max_length=500, null=False, unique=True)
    account_number = models.IntegerField(null=True)
    account_name = models.CharField(max_length=200,null=True)
    bank = models.CharField(max_length=200,null=True)
    poster = models.ImageField(upload_to='media',null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Event(models.Model):
    entertainment = 'Entertainment'
    tech = 'Tech'
    professional = 'Professional'
    religious = 'Religious'
    STATUS = [
       (entertainment, ('Entertainment')),
       (tech, ('Tech')),
       (professional, ('Professional')),
       (religious, ('Religious')),
   ]
    title = models.CharField(max_length=500)
    venue = models.CharField(max_length=1000, null=True)
    description = models.TextField()
    creator = models.ForeignKey(Organizer, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=STATUS, null=True)
    poster = models.ImageField(null=True, blank=False, upload_to='media')
    ticket_price = models.FloatField(null=True)
    tickets_ava  = models.IntegerField(blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    views = models.IntegerField(default=0)

    slug = models.SlugField(max_length=500, null=False, unique=True)
    # earnings = models.FloatField(null=True)

    
    def earnings(self):
        return self.Ticket * self.ticket_price
    class Meta:
        ordering = [ '-created']

    def __str__(self):
        return self.title

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tix_code = models.CharField(max_length=500, null=True, unique=True)
    tix_mail = models.CharField(max_length=500, null=True)
    tix_name = models.CharField(max_length=500, null=True)
    tix_phone = models.CharField(max_length=500, null=True)
    ticket_price = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    # def total_tix(self):
    #     return self.count() * self.ticket_price

    def __str__(self):
        return self.event.title +  "; " + self.tix_code

class Media(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photos = models.ImageField(null=True, blank=False, upload_to='media')

    def __str__(self):
        return self.event.title 

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.event.title +  "; " + self.comment

class Bookmark(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title

class CustomerInfo(models.Model):
    full_name= models.CharField(max_length  = 150)
    email= models.EmailField()
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length = 150)