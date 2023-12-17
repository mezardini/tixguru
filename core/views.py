from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Event, Ticket, Bookmark
from .serializers import EventSerializer, TicketSerializer, UserSerializer, BookmarkSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics, status, viewsets
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core import mail
from django.conf import settings
import random


@api_view(['GET'])
def index(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def eventCreate(request):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer = EventSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def eventDelete(request, pk):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    event = Event.objects.get(id=pk)
    event.delete()

    return Response('Item deleted!')

@api_view(['POST'])
def eventUpdate(request, pk):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()




class CreateTicket(generics.CreateAPIView):
    serializer_class = TicketSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, pk):
        event = self.get_event(pk)
        if not event:
            return Response({'error': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)

        mail = request.data.get("tix_mail")
        name = request.data.get("tix_name")
        code = self.generate_ticket_code()
        
        data = {'event': pk, 'tix_mail': mail, 'tix_code': code, 'tix_name': name}
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            self.send_ticket_confirmation(mail, name, event.title, code)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_event(self, event_id):
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return None

    def generate_ticket_code(self):
        return "#" + "-" + str(random.randint(1000, 123999999))

    def send_ticket_confirmation(self, recipient_email, recipient_name, event_title, ticket_code):
        subject = 'Ticket booked!!!'
        message = f'Hello {recipient_name}, your ticket for the event {event_title} has been booked, and your code is {ticket_code}'
        from_email = 'settings.EMAIL_HOST_USER'  
        recipient_list = [recipient_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)



class EventList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Event.objects.filter(creator_id=self.kwargs["pk"])
        return queryset

    serializer_class = EventSerializer


class TicketList(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Event.objects.filter(creator_id=self.kwargs["pk"])
        tickets = Ticket.objects.filter(event__creator=self.kwargs["pk"]).order_by('-id')
        return tickets
    
    serializer_class = TicketSerializer


class CreateBookmark(generics.CreateAPIView):
    serializer_class = BookmarkSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, pk):
        
        user_ip_address = self.get_user_ip_address(request)
        
        
        bookmark_data = {'event': pk, 'creator': user_ip_address}
        
        
        serializer = self.get_serializer(data=bookmark_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_user_ip_address(self, request):
        
        return request.META.get('REMOTE_ADDR')


class BookmarkList(generics.ListCreateAPIView):

    
    
    def get_queryset(self):
        self.request.user = '127.0.0.1'
        queryset = Bookmark.objects.filter(creator=self.request.user)
        return queryset
    
    serializer_class = BookmarkSerializer