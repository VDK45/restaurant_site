from django import template

from restaurant.models import *

register = template.Library()


@register.simple_tag(name='get_list_cat')  # Скобки необязтельно
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('restaurant/list_categories.html')
def show_categories(arg1='Hello ', arg2='world!'):
    categories = Category.objects.all()
    return {"categories": categories, 'arg1': arg1, 'arg2': arg2}
