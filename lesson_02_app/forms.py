"""
Задание №3
    📌 Продолжаем работу с авторами, статьями и комментариями.
    📌 Создайте форму для добавления нового автора в базу
    данных.
    📌 Используйте ранее созданную модель Author

Задание №4
    📌 Аналогично автору создайте форму добавления новой
    статьи.
    📌 Автор статьи должен выбираться из списка (все доступные в
    базе данных авторы).
"""

from django import forms
from . import models
import datetime

class AuthorForm(forms.Form):
    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                                  'placeholder': 'Имя автора: ',
                                                                                  'size': '320px'}))
    lastname = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                                    'placeholder': 'Фамилия автора:'}))
    email = forms.EmailField(initial='E-mail:', label='',
                             widget=forms.EmailInput(attrs={'class': 'input_text long_input'}))
    biography = forms.CharField(initial='биография', label='',
                          widget=forms.Textarea(attrs={'class': 'input_text long_input'}))
    birthday = forms.DateField(initial=datetime.date.today, label='',
                                widget=forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'}))

""" Это рабочий класс, просто разные варианты
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    #Способ 1 - кортежи циклом
    #choices = [(i.id, i.fullname()) for i in models.Author.objects.all()]
    #author = forms.ChoiceField(choices=choices)
    #Способ 2 - queryset
    author = forms.ModelChoiceField(queryset=models.Author.objects.all(), empty_label='Выберите автора:')
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input_text long_input'}))
    created_date = forms.DateField()
    category = forms.CharField(max_length=100)
"""

#Способ 3 - ModelForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'author', 'content', 'created_date']
        labels = {'title': '', 'author': '', 'content': '', 'created_date': ''}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_text long_input', 'placeholder': 'Название статьи:'}),
            'author': forms.Select(attrs={'class': 'input_text long_input'}),
            'content': forms.Textarea(
                attrs={'class': 'input_text long_input', 'cols': 100, 'rows': 10, 'placeholder': 'Содержание статьи'}),
            'created_date': forms.DateInput(attrs={'class': 'input_text long_input', 'type': 'date'}),
        }   

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=models.Author.objects.all(), empty_label='Автор комментария:')
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input_text long_input'}))
  

    