from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('greet/me/', views.greet, name='greet_me'),
]