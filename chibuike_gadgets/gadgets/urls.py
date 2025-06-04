from django.urls import path

from . import views

urlpatterns = [
    path('gadgets/', views.gadgets_we_sell, name="our_gadgets"),
]