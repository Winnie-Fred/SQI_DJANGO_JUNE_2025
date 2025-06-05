from django.urls import path

from . import views

urlpatterns = [
    path("demo/", views.demo_inheritance, name='demo_inheritance'),
]