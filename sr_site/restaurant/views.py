from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    menu = Menu.objects.all()  #
    # menu = Menu.objects.order_by('-created_at')  # Sort by new if not sorty in Meta
    context = {
        'title': 'All menu',  # tittle (index.html)
        'menu': menu,  # body (index.html)
    }
    return render(request, template_name='restaurant/index.html', context=context)



