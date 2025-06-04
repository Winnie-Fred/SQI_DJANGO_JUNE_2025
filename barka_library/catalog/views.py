from django.shortcuts import render, HttpResponse

# Create your views here.
def all_books(request):
    return HttpResponse("""
    <h3>All Books</h3>
    
    <ul>
        <li>Things Fall Apart</li>                    
        <li>Murder on the Orient Express</li>                    
        <li>The Murder of Roger Ackroyd</li>                    
        <li>A good girl's guide to Murder</li>                    
        <li>The Secret</li>                    
    </ul>
""")

def featured_books(request):
    return HttpResponse("""
    <h3>Featured Books</h3>
    <div>
        <li>Animal Farm</li>                    
        <li>This Thing Called Purpose</li>                    
    </div>
""")