from django.contrib import admin
from .models import Event,  Ticket, Bookmark
# Register your models here.


admin.site.register(Event)
admin.site.register(Bookmark)
admin.site.register(Ticket)