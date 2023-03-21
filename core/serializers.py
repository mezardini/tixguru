from rest_framework.serializers import ModelSerializer
from .models import Event, Ticket, Bookmark
from django.contrib.auth.models import User


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'