from django.shortcuts import render, HttpResponse

# Create your views here.
def gadgets_we_sell(request):
    return HttpResponse("""
    <ol>
        <li>TV</li>                   
        <li>DSTV</li>                   
        <li>Washing Machine</li>                   
        <li>Blender</li>                   
    </ol>
""")