from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


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


# def get_category(request, category_id):
#     menu = Menu.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     # category = Category.objects.get(pk=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     return render(request, 'restaurant/category.html',
#                   {'menu': menu, 'category': category, 'title': 'Menu'})


class ViewGame(DetailView):
    model = Games
    template_name = 'restaurant/view_game_class.html'  # custom file home_menu_list.html
    pk_url_kwarg = 'game_id'
    context_object_name = 'game'


# def view_game(request, game_id):
#     # game = Games.objects.get(pk=game_id)
#     game = get_object_or_404(Games, pk=game_id)
#     return render(request, 'restaurant/game.html', {'game': game})


class ViewMenu(DetailView):
    model = Menu
    template_name = 'restaurant/view_menu_class.html'  # custom file home_menu_list.html
    pk_url_kwarg = 'pk'  # 'pk' Вместо 'menu_id'
    context_object_name = 'menu'


# def view_menu(request, menu_id):
#     # menu_item = Menu.objects.get(pk=menu_id)
#     menu_item = get_object_or_404(Menu, pk=menu_id)
#     return render(request, 'restaurant/view_menu.html', {"menu_item": menu_item})


class AddMenu(CreateView):
    form_class = MenuForms
    template_name = 'restaurant/add_menu_class.html'
    context_object_name = 'form'
    # success_url = reverse_lazy('home')  # if get_absolute_url not exist


# def add_menu(request):
#     if request.method == 'POST':
#         form = MenuForms(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # new_menu = Menu.objects.create(**form.cleaned_data)  # распаковка  # Формы не связаны с models
#             new_menu = form.save()  # Формы связаны с models
#             return redirect(new_menu)
#     else:
#         form = MenuForms()
#     return render(request, 'restaurant/add_menu.html', {'form': form})


class SearchResultsView(ListView):
    model = Menu
    template_name = 'search_results.html'
