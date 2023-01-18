from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('browse', views.browse, name="browse"),
    path('event/<str:slug>', views.details, name="details"),
    path('create_event', views.create_event, name="create_event"),
    path('ticket/<str:pk>', views.bookmark, name="bookmark"),
    path('organizer', views.organizer, name="organizer"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name='signout'),
    path('sendmail/<str:slug>', views.sendmail, name='sendmail'),
    path('adminview/<str:slug>', views.admin_details, name='adminview'),
    path('profile/<str:slug>', views.profile, name='profile'),
    path('deleteevent/<str:slug>', views.delete_event, name='deleteevent'),
    path('callback', views.payment_response, name='payment_response'),
    
]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    