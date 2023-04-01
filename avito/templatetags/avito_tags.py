from django import template
from avito.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('avito/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.filter(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('avito/list_menu.html')
def show_main_menu():
    menu = [
        {'title': 'Главная страница', 'url_name': 'main'},
        {'title': 'Создать объявление', 'url_name': 'add_ad'},
        {'title': 'О сайте', 'url_name': 'about'},
    ]

    return {'menu': menu}
