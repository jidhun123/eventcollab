from django.urls import path
from .views import UserListCreateView, EventListCreateView, EventDetailInviteView
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailInviteView.as_view(), name='event-detail-invite'),
]
