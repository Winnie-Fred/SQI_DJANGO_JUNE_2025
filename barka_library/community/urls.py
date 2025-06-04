from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.upcoming_community_events, name='upcoming_community_events'),
]