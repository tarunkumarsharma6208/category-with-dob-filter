from django.urls import path
from . import views
urlpatterns = [
    path('dob/', views.dobFilter, name='dobFilter'),
    path('articles/', views.articles_list, name='articles'),
    path('articles/<slug:category_slug>/', views.articles_list, name='article_by_category'),
    path('articles/<slug:cat_slug>/<slug:slug>/', views.detail_article, name='detail_article'),
]