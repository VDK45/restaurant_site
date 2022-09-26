from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    menu = Menu.objects.all()  #
    # categories = Category.objects.all()
    # menu = Menu.objects.order_by('-created_at')  # Sort by new if not sorty in Meta
    context = {
        'title': 'Menu',  # tittle (index.html)
        'menu': menu,  # body (index.html)
    }
    return render(request, template_name='restaurant/index.html', context=context)


def get_category(request, category_id):
    menu = Menu.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'restaurant/category.html',
                  {'menu': menu, 'category': category, 'title': 'Menu'})


def get_game(request, game_id):
    game = Games.objects.filter(pk=game_id)
    return render(request, 'restaurant/game.html', {'game': game[0], 'title': game_id})

