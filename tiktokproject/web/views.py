from django.shortcuts import render
from tiktokproject import settings



# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

    
    