"""
📌 Создайте пару представлений в вашем первом приложении:
главная и о себе.
📌 Внутри каждого представления должна быть переменная
html - многострочный текст с HTML вёрсткой и данными о
вашем первом Django сайте и о вас.
📌 *Сохраняйте в логи данные о посещении страниц
"""
import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def my_first_django(request):
    html = '<h1>Мой первый Django сайт</h1>\
            <p>Ура, получилось!</p>'
    logger.info('Страницу с первым Django сайтом кто-то посетил')
    return HttpResponse(html)


def about(request):
    html = '<h1>Страница обо мне</h1>\
            <p>Меня зовут Анна.</p>'
    logger.info('Страницу обо мне кто-то посетил')
    return HttpResponse(html)    