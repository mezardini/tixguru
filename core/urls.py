from django.urls import path
from . import views
from .views import CreateTicket, EventList, TicketList, CreateBookmark, BookmarkList
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:pk>', views.eventDetail, name="detail"),
    path('create', views.eventCreate, name="create"),
    path('delete/<int:pk>', views.eventDelete, name="delete"),
    path('update/<int:pk>', views.eventUpdate, name="update"),
    path("detail/<int:pk>/create-ticket",
         CreateTicket.as_view(), name="createTicket"),
    path("profile/<int:pk>/events/", EventList.as_view(), name="event_list"),
    path("profile/<int:pk>/tickets/", TicketList.as_view(), name="ticket_list"),
    path("detail/<int:pk>/create-bookmark",
         CreateBookmark.as_view(), name="CreateBookmark"),
    path("ip/events/", BookmarkList.as_view(), name="bookmark_list"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
