from django.shortcuts import render, HttpResponse

# Create your views here.
def upcoming_community_events(request):
    return HttpResponse("""
    <section>
        <div>Our Annual Book Club is coming up next week on Monday by 4:00 p.m</div>                    
        <div>Our Book Signings hold on Saturdays and Sunday by 6:00 p.m</div>                    
    </section>
""")