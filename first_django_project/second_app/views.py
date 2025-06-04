from django.shortcuts import render, HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("<h1>Contact us at sqi@sqi.edu.ng</h1>")