from django import template
from restaurant.models import *
from django.db.models import Count, F

register = template.Library()


@register.simple_tag(name='get_list_cat')  # Скобки необязательно
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('restaurant/list_categories.html')
def show_categories(arg1, arg2):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('menu')).filter(cnt__gt=0)  # show category have 1 more menu
    return {"categories": categories, 'arg1': arg1, 'arg2': arg2}


@register.inclusion_tag('restaurant/list_games.html')
def show_games(arg1):
    games = Games.objects.all()
    return {"games": games, 'arg1': arg1}
