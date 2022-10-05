# Основной файл url
from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='home'),  # func index from views
    path('', HomeMenu.as_view(), name='home'),  # class HomeMenu from views
    path('category/<int:category_id>/', get_category, name='category'),
    path('game/<int:game_id>/', get_game, name='game'),
    path('menu/<int:menu_id>/', get_menu, name='show_menu'),
    path('add_menu/', add_menu, name='add_menu'),

]
