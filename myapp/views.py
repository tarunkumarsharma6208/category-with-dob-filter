import datetime
from django.shortcuts import render, get_object_or_404
from .models import *


def dobFilter(request):
    obj = Profile.objects.all().filter(dob__lte=datetime.date(1981, 1, 10))
    return render(request, 'index.html', {'obj': obj})


def articles_list(request, category_slug=None):
    category_page = None
    articles = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        articles = Article.objects.filter(category=category_page)
    else:
        articles = Article.objects.all()
    return render(request, 'articles.html', {'category': category_page, 'articles': articles})


def detail_article(request, cat_slug, slug):
    obj = get_object_or_404(Article, category__slug=cat_slug, slug=slug)
    return render(request, 'detail.html', {'obj': obj})