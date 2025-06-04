from django.shortcuts import render

# Create your views here.
def dtl_view(request):
    context = {
        'name': 'Winnie',
        'age': 32,
        'is_female': False,
        'courses_instructed': ["Django", "Python", "HTML", "Flutter", "Git", "JS"],
        'cohorts': {
            'Python May Cohort': 5,
            'Django June Cohort': 8,
        }
    }
    return render(request, "dtl/dtl-html.html", context)