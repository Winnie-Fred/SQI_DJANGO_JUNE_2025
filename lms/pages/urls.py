from django.urls import path

from . import views

app_name = 'pages'


urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about_our_company'),
    path('contact-us/', views.contact, name='contact_info'),
]