from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView


# Create your views here.
class HomeMenu(ListView):
    model = Menu   # file  menu_list.html
    template_name = 'restaurant/home_menu_list.html'  # custom file home_menu_list.html
    context_object_name = 'all_menu'
    # extra_context = {'title': 'Trang chu'}  # for static data only

    def get_context_data(self, *, object_list=None, **kwargs):  # для контекстов
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trang chu'
        return context

    def get_queryset(self):
        return Menu.objects.filter(is_published=True)   # Show is_published only


class CategoryMenu(ListView):
    model = Menu
    template_name = 'restaurant/home_category_list.html'  # custom file home_menu_list.html
    context_object_name = 'category_menu'
    allow_empty = False  # Не показывать несушествующие категории

    def get_context_data(self, *, object_list=None, **kwargs):  # для контекстов
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Menu.objects.filter(is_published=True, category_id=self.kwargs['category_id'])   # Show is_published only


# def index(request):
#     menu = Menu.objects.all()  #
#     categories = Category.objects.all()
#     # menu = Menu.objects.order_by('-created_at')  # Sort by new if not sorty in Meta
#     context = {
#         'title': 'Trang chu',  # tittle (index.html)
#         'menu': menu,  # body (index.html)
#     }
#     return render(request, template_name='restaurant/index.html', context=context)


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
            # new_menu = Menu.objects.create(**form.cleaned_data)  # распаковка  # Формы не связаны с models
            new_menu = form.save()  # Формы связаны с models
            return redirect(new_menu)
    else:
        form = MenuForms()
    return render(request, 'restaurant/add_menu.html', {'form': form})
