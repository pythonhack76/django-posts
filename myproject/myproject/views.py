#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello World!")
    return render(request, 'home.html')


    
def about(request):
    #return HttpResponse("La nostra pagine about.")
    return render(request, 'about.html')

