"""
Задание №6
    📌 Создайте форму для редактирования товаров в базе данных.
"""
from django import forms
from . import models

class ProductForm(forms.Form):
    name = forms.CharField(label='Название товара', max_length=40)
    description = forms.CharField(label='Описание',
                          widget=forms.Textarea(attrs={'class': 'input_text long_input'}))
    price = forms.DecimalField(max_digits=9, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField()