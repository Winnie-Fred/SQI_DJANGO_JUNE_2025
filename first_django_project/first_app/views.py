from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the home page!!!")


def greet(request):
    return HttpResponse("Good morning, Winnie")