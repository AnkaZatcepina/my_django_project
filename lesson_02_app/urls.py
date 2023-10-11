from django.urls import path, include
from . import views 

articles_patterns = [
    path('', views.get_articles, name='articles'),
    path('comments/', views.get_comments, name='comments'),
    path('by_author/', views.get_articles_by_author, name='articles_by_author'),
    path('<int:article_id>/', views.get_article, name='get_article'),
]

urlpatterns = [ 
    #path('', views.index, name='index'), 
    path('random_coin/', views.random_coin, name='random_coin'), 
    path('get_last_coins/', views.get_last_coins, name='get_last_coins'), 
    path('authors/', views.get_authors, name='authors'),
    path('articles/', include(articles_patterns)),
    path('create_author/', views.create_author, name='create_author'),
    path('create_article/', views.create_article, name='create_article'),
    ]