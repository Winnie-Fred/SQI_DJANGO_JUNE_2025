from django.shortcuts import render

# Create your views here.
services = {
    "Django-powered websites": 1500,
    "Static websites": 500,
    "API Development with DRF": 2000,
    "Hosting and Deployment": 200,
    "Consultancy": 1200
}
def services_offered(request):
    services_list = list(services.keys())
    context = {"services": services_list}
    return render(request, "portfolio/services.html", context)


def testimonials(request):
    customer_testimonials = {
        "Winnie": "I loved this developer's services.",
        "Abeeb": "Awesome service. Rapid response",
        "Usman": "Not bad, I've seen better",
        "Haleem": "I employed this devloper's service in 2005 and the site is still running up till now with no hassle.",
        "Mrs. Akintola": "Bad service. Hardly responds. 😡"
    }
    context = {
        "customer_testimonials": customer_testimonials
    }
    return render(request, "portfolio/testimonials.html", context)


def pricing(request):
    return render(request, "portfolio/pricing.html", {'pricing': services})

def blog(request):
    return render(request, "portfolio/blog.html")

def case_studies(request):
    return render(request, "portfolio/case-studies.html")