from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    # menu = Menu.objects.all()  #
    menu = Menu.objects.order_by('-created_at')  # Sort by new
    context = {
        'menu': menu,
        'title': 'Menu'
    }
    return render(request, template_name='restaurant/index.html', context=context)



