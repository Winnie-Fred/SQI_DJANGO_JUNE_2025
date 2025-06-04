from django.urls import path

from . import views

urlpatterns = [
    path('phone/', views.phone_us, name='phone'),
    path('email/', views.email_us, name='email'),
]