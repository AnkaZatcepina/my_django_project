"""
📌 Создайте новое приложение. Подключите его к проекту. В
приложении должно быть три простых представления,
возвращающих HTTP ответ:
📌 Орёл или решка
📌 Значение одной из шести граней игрального кубика
📌 Случайное число от 0 до 100
📌 Пропишите маршруты

📌 Добавьте логирование в проект.
📌 Настройте возможность вывода в файл и в терминал.
📌 Устраните возможные ошибки.

Задание №3
📌 Маршруты могут принимать целое число - количество
бросков.
📌 Представления создают список с результатами бросков и
передают его в контекст шаблона.
📌 Необходимо создать универсальный шаблон для вывода
результатов любого из трёх представлений.

Задание №4
📌 Доработаем задачу про броски монеты, игральной кости и
случайного числа.
📌 Создайте форму, которая предлагает выбрать: монета, кости,
числа.
📌 Второе поле предлагает указать количество попыток от 1 до 64.
"""
import logging
import random
from django.shortcuts import render
from django.http import HttpResponse 
from . import forms
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

def random_coin(request, count: int): 
    answer = ['Орёл', 'Решка']
    result = []
    for _ in range(count):
        result.append(random.choice(answer))
    logger.info(result)
    content = {
        'items': result,
        'count': count
    }
    return render(request, "lesson_01_task_2_app/random.html", content) 
    
def random_dice(request, count: int):
    result = []
    for _ in range(count):
        result.append(random.randint(1, 7))
    logger.info(result) 
    content = {
        'items': result,
        'count': count
    }
    return render(request, "lesson_01_task_2_app/random.html", content)

def random_hundred(request, count: int): 
    result = []
    for _ in range(count):
        result.append(random.randint(0, 101))
    logger.info(result)
    content = {
        'items': result,
        'count': count
    }
    return render(request, "lesson_01_task_2_app/random.html", content)   

def choice_game_form(request):
    if request.method == 'POST':
        form = forms.ChoiceGameForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            count = form.cleaned_data['count']
            if choice == 'C':
                return random_coin(request, count)
            elif choice == 'D':
                return random_dice(request, count)
            elif choice == 'H':    
                return random_hundred(request, count)
    else:
        form = forms.ChoiceGameForm()
    return render(request, 'lesson_01_task_2_app/choice_game_form.html', {'form':form})   
