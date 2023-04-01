from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .froms import *
from .models import *
from .utils import *

# Create your views here.


class AvitoMain(DataMixin, ListView):
    model = Ad
    template_name = 'avito/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Ad.objects.filter(is_published=True)
# def index(request):
#     posts = Ad.objects.all()
#
#     context = {
#         'title': 'Главная страница',
#         'posts': posts,
#         'cat_selected': 0
#     }
#     return render(request, 'avito/index.html', context=context)


def about(request):
    return render(request, 'avito/about.html', {'title': 'О сайте'})


class AddAd(CreateView):
    form_class = AddAdForm
    template_name = 'avito/add_ad.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление объявления'
        return context
# def add_ad(request):
#     if request.method == 'POST':
#         form = AddAdForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     else:
#         form = AddAdForm()
#
#     return render(request, 'avito/add_ad.html', {'form': form, 'menu': menu, 'title': 'Добавление объявления'})


# def login(request):
#     return HttpResponse('Login')


class ShowAd(DetailView):
    model = Ad
    template_name = 'avito/post.html'
    slug_url_kwarg = 'ad_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context
# def show_ad(request, ad_slug):
#     post = get_object_or_404(Ad, slug=ad_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'avito/post.html', context=context)


class AvitoCategory(DataMixin, ListView):
    model = Ad
    template_name = 'avito/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Ad.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
# def show_category(request, cat_id):
#     posts = Ad.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'title': 'Отображение по рубрикам',
#         'posts': posts,
#         'cat_selected': cat_id
#     }
#     return render(request, 'avito/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'avito/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'avito/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('main')
