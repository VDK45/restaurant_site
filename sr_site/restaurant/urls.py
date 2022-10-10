# Основной файл url
from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='home'),  # func index from views
    path('', HomeMenu.as_view(), name='home'),  # class HomeMenu from views
    # path('category/<int:category_id>/', get_category, name='category'),
    # path('category/<int:category_id>/', CategoryMenu.as_view(extra_context={'title': 'title'}), name='category'),
    path('category/<int:category_id>/', CategoryMenu.as_view(), name='category'),
    # path('game/<int:game_id>/', view_game, name='game'),
    path('game/<int:game_id>/', ViewGame.as_view(), name='game'),
    # path('menu/<int:menu_id>/', view_menu, name='show_menu'),
    path('menu/<int:pk>/', ViewMenu.as_view(), name='show_menu'),
    # path('add_menu/', add_menu, name='add_menu'),
    path('add_menu/', AddMenu.as_view(), name='add_menu'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
