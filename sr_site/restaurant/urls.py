# Основной файл url
from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    # path('', index, name='home'),  # func index from views
    path('', HomeMenu.as_view(), name='home'),  # class HomeMenu from views
    # path('category/<int:category_id>/', get_category, name='category'),
    # path('category/<int:category_id>/', CategoryMenu.as_view(extra_context={'title': 'title'}), name='category'),
    path('category/<int:category_id>/', CategoryMenu.as_view(), name='category'),
    # path('game/<int:game_id>/', view_game, name='game'),
    path('game/<int:game_id>/', ViewGame.as_view(), name='game'),
    # path('menu/<int:menu_id>/', view_menu, name='show_menu'),
    path('menu/<int:pk>/', ViewMenu.as_view(), name='show_menu'),  # cache_page(600)()
    # path('add_menu/', add_menu, name='add_menu'),
    path('add_menu/', AddMenu.as_view(), name='add_menu'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('comment/', CommentAdded.as_view(), name='comment'),
    path('error/', error_page, name='error'),
    # path('accounts/login/', account_user_login, name='account_login'),

]
