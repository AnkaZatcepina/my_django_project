from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404 
from django.template.response import TemplateResponse
import random
from . import models
from . import forms
from django.contrib import messages
  
def random_coin(request): 
    answer = ['Орёл', 'Решка']
    result = random.choice(answer)
    result_m = models.Coin(result=result)
    result_m.save()
    return HttpResponse(result_m) 

def get_last_coins(request): 
    n = request.GET.get('n', '5')
    return HttpResponse(models.Coin.statistic(int(n)).items())   

def get_authors(request): 
    authors = models.Author.objects.all()
    #result = '\n'.join(str(author) for author in authors)
    return HttpResponse(authors)     

def get_articles(request): 
    articles = models.Article.objects.all()

    context = {"articles": articles}
    return render(request, "lesson_02_app/articles.html", context)
    #return HttpResponse(articles)   

def get_article(request, article_id: int): 
    article = get_object_or_404(models.Article, pk=article_id)
    article.show_count += 1
    article.save()
    comments = models.Comment.objects.filter(article_id=article_id).order_by('-modificated_date')
    if request.method == 'POST':
        form_comment = forms.CommentForm(request.POST)
        if form_comment.is_valid():
            comment = models.Comment(author=form_comment.cleaned_data['author'],
                                    article=article,
                                    content=form_comment.cleaned_data['content'],
            )
            comment.save()
    else:
        form_comment = forms.CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form_comment': form_comment,
    }

    return render(request, "lesson_02_app/article_detail.html", context)    

#/lesson2/articles/by_author?name=Name2
def get_articles_by_author(request): 
    author_id = None
    name = request.GET.get('name')
    author = models.Author.objects.filter(name=name).first()
    if author:
        author_id = author.pk 

    articles = models.Article.objects.filter(author=author)
    #articles = models.Article.objects.filter(author_id=author_id)
    #articles = models.Article.objects.filter(author__pk=author_id)

    return HttpResponse(articles)          

def get_comments(request): 
    comments = models.Comment.objects.all()
    return HttpResponse(comments)    

def create_author(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = models.Author(name=form.cleaned_data['name'],
                            lastname=form.cleaned_data['lastname'],
                            email=form.cleaned_data['email'],
                            biography=form.cleaned_data['biography'],
                            birthday=form.cleaned_data['birthday'])
            author.save()
            messages.add_message(request, messages.SUCCESS, 'Успешно')
    else:
        form = forms.AuthorForm()
    return TemplateResponse(request, 'lesson_02_app/template_form.html', context={'form': form})

def create_article(request):
    if request.method == 'POST':
        form = forms.ArticleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.ArticleForm()
    return TemplateResponse(request, 'lesson_02_app/template_form.html', context={'form': form})
    
