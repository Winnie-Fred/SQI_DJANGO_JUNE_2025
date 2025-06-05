from django.shortcuts import render

# Create your views here.
def demo_inheritance(request):
    return render(request, "inheritance_correction/demo.html")