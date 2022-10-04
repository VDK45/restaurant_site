from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(request):
    menu = Menu.objects.all()  #
    categories = Category.objects.all()
    # menu = Menu.objects.order_by('-created_at')  # Sort by new if not sorty in Meta
    context = {
        'title': 'Trang chu',  # tittle (index.html)
        'menu': menu,  # body (index.html)
    }
    return render(request, template_name='restaurant/index.html', context=context)


def get_category(request, category_id):
    menu = Menu.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'restaurant/category.html',
                  {'menu': menu, 'category': category, 'title': 'Menu'})


def get_game(request, game_id):
    # game = Games.objects.get(pk=game_id)
    game = get_object_or_404(Games, pk=game_id)
    return render(request, 'restaurant/game.html', {'game': game})


def get_menu(request, menu_id):
    # menu_item = Menu.objects.get(pk=menu_id)
    menu_item = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'restaurant/view_menu.html', {"menu_item": menu_item})


def add_menu(request):
    if request.method == 'POST':
        form = MenuForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new_menu = Menu.objects.create(**form.cleaned_data)  # распаковка
            return redirect(new_menu)
    else:
        form = MenuForms()
    return render(request, 'restaurant/add_menu.html', {'form': form})
