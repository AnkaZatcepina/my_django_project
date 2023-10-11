"""
Задание №1
    📌 Создайте модель для запоминания бросков монеты: орёл или решка.
    📌 Также запоминайте время броска
Задание №2    
    📌 Добавьте статический метод для статистики по n последним броскам монеты.
    📌 Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
Задание №3
    📌 Создайте модель Автор. Модель должна содержать следующие поля:
        ○ имя до 100 символов
        ○ фамилия до 100 символов
        ○ почта
        ○ биография
        ○ день рождения
    📌 Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.    
Задание №4
    📌 Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи. 
    У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
        ○ заголовок статьи с максимальной длиной 200 символов
        ○ содержание статьи
        ○ дата публикации статьи
        ○ автор статьи с удалением связанных объектов при удалении автора
        ○ категория статьи с максимальной длиной 100 символов
        ○ количество просмотров статьи со значением по умолчанию 0
        ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False
Задание №5
    📌 Создай четыре функции для реализации CRUD в модели Django Article (статья).
    📌 *Используйте Django команды для вызова функций.     
Задание №6
    📌 Создайте модель Комментарий.
    📌 Авторы могут добавлять комментарии к своим и чужим статьям. 
        Т.е. у комментария может быть один автор.
    📌 И комментарий относится к одной статье. У модели должны быть следующие поля
        ○ автор
        ○ статья
        ○ комментарий
        ○ дата создания
        ○ дата изменения   
"""
from django.db import models
from django.utils import timezone

class Coin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=5)

    def __str__(self):
        return f'time: {self.created_at}, result: {self.result}'

    @staticmethod
    def statistic(n: int):
        query = list(Coin.objects.all())
        coins = query[-n:]
        coins_dict = {'Орёл': 0, 'Решка': 0}
        for item in coins:
            if 'Орёл' in str(item):
                coins_dict['Орёл'] += 1
            else:
                coins_dict['Решка'] += 1
        return coins_dict

class Author(models.Model):
    name = models.CharField(max_length = 100)      
    lastname = models.CharField(max_length = 100)    
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()   

    def fullname(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'{self.pk}, {self.name} {self.lastname}, {self.email}'   

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}, {self.is_published}, {self.author}: {self.content[:20]}...'

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modificated_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.content}, {self.author.id}, {self.article.id}, {self.created_date}'
