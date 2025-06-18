from django.urls import path

from . import views

# app_name = "recipe"

urlpatterns = [
    path('list/', views.recipe_list, name='recipe_list'),
    path('new/', views.recipe_create, name='recipe_create'),
]