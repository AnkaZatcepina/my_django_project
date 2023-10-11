from django.core.management.base import BaseCommand
from ... import models
import random

class Command(BaseCommand):
    help = "Generate fake authors and articles"
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='amount')
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = models.Author(
                name=f'Name{i}', 
                lastname=f'LastName{i}',      
                email=f'mail{i}@mail.ru',
                biography=f'bio{i}',
                birthday=f'2023-09-26',
            )
            author.save()
            for j in range(1, count + 1):
                article = models.Article(
                    title=f'Title{j}', 
                    content=f'Text from {author.name} #{j} is bla bla bla many long text',
                    created_date='2023-09-26', 
                    author=author,
                    category=f'Category{j}',
                    is_published = random.choice([True,False])
                )
                article.save()
        for i in range(1, count * 5 + 1):
            random_author = models.Author.objects.order_by('?')[0]
            random_article = models.Article.objects.order_by('?')[0]            
            comment = models.Comment(
                author = random_author,
                article = random_article,
                content = f'Comment{i}'
            )
            comment.save()
        