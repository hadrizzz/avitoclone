from .models import *

menu = [
        {'title': 'Главная страница', 'url_name': 'main'},
        {'title': 'Создать объявление', 'url_name': 'add_ad'},
        {'title': 'О сайте', 'url_name': 'about'},
    ]


class DataMixin:

    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
