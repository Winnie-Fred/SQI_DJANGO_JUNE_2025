from django.shortcuts import render, HttpResponse

# Create your views here.
def phone_us(request):
    return HttpResponse("<h1>Call us: +2349030556523</h1>")

def email_us(request):
    return HttpResponse("<h3>Email us: sqirestaurant@gmail.com</h3>")

