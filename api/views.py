from rest_framework import generics
from .models import User, Event
from .serializers import UserSerializer, EventSerializer
from django.shortcuts import render

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailInviteView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'
    
def index(request):
    return render(request, 'index.html')