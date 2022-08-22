from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .utils import MyMixin
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout

# def test(request):
#     object_context_list = ['News 1', 'News 2', 'News 3', 'News 4', 'News 5', 'News 6', 'News 7', 'News 8']
#     paginator = Paginator(object_context_list, 2)
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'news/test.html', {'page_obj': page_obj})

# def test(request):
#     form = TestForm(request.POST)
#     return render(request, 'news/test.html', {'form': form})

def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешно!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm() 

    context = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'news/register.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка входа в аккаунт')
    else:
        form = UserLoginForm()

    context = {
        'title': 'Вход в аккаунт',
        'form':form
    }
    return render(request, 'news/login.html', context)


class NewsView(MyMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2
    # 1, 2 mixin_prop = 'hello world'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список новостей'
        # 1 context['mixin_prop'] = self.get_prop()
        # 2 context['mixin_prop'] = self.get_upper('hello world')
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryView (ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Новости на тему: {Category.objects.get(pk=self.kwargs['category_id'])}"
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id']).select_related('category')


class NewsDetail(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{News.objects.get(pk=self.kwargs['pk'])}"
        return context
        
    def get_queryset(self):
        return News.objects.select_related('category')


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    extra_context = {'title': 'Добавление новости'}
    login_url = '/admin/'
    # raise_exception = True


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(f'view_news', news_id=news.pk)
#     else:
#         form = NewsForm()
#     context = {'title': "Добавление новости", 'form': form}
#     return render(request, 'news/add_news.html', context)


# def index(request):
#     news = News.objects.all()
#     context = {
#         'title':'Список новостей',
#         'news': news,
#         }
#     return render(request, 'news/index.html', context)
 

# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = get_object_or_404(Category, pk=category_id)
#     context = {
#         'title':f'Новости на тему: {category.title}',
#         'news': news,
#         }
#     return render(request, 'news/category.html', context)


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         'title': news_item.title,
#         'news_item': news_item
#         }
#     return render(request, 'news/view_news.html', context)

