from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin  # for login users only
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout


# Create your views here.
class HomeMenu(MyMixin, ListView):
    model = Menu   # file  menu_list.html
    template_name = 'restaurant/home_menu_list.html'  # custom file home_menu_list.html
    context_object_name = 'all_menu'
    mixin_prop = ''
    # extra_context = {'title': 'Trang chu'}  # for static data only
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):  # для контекстов
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('trang chu')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return Menu.objects.filter(is_published=True).select_related('category')


class CategoryMenu(MyMixin, ListView):
    model = Menu
    template_name = 'restaurant/home_category_list.html'  # custom file home_menu_list.html
    context_object_name = 'category_menu'
    allow_empty = False  # Не показывать несушествующие категории
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):  # для контекстов
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return Menu.objects.filter(is_published=True, category_id=self.kwargs['category_id']).select_related('category')


class SearchResultsView(ListView):
    model = Menu
    # template_name = 'restaurant/add_menu_class.html'
    template_name = 'restaurant/SearchResultsView.html'
    # queryset = Menu.objects.filter(name__icontains='la')
    # paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Menu.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )[:4]
        return object_list


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


class AddMenu(LoginRequiredMixin, CreateView):
    form_class = MenuForms
    template_name = 'restaurant/add_menu_class.html'
    context_object_name = 'form'
    # success_url = reverse_lazy('home')  # if get_absolute_url not exist
    # raise_exception = True  # Если не авторизован то ERROR 403
    login_url = '/admin/'  # Если не авторизован то к странице Админ


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


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Сразу вошел как авторизованый
            messages.success(request, 'Cảm ơn bạn đã đăng ký!')
            return redirect('home')
        else:
            messages.error(request, 'Xin bạn làm ơn chỉnh lại phần đăng ký!')

    else:
        form = UserRegisterForm()

    return render(request, 'restaurant/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # data= (Обязательно)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'restaurant/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')

