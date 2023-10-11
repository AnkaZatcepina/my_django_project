from django.core.management.base import BaseCommand
from ... import models

#python3 manage.py create_author Luke Cage test@mail.ru 'big biography text' 2023-11-11
class Command(BaseCommand):
    help = "Create"
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name')
        parser.add_argument('lastname', type=str, help='last name')
        parser.add_argument('email', type=str, help='email')
        parser.add_argument('biography', type=str, help='biography')
        parser.add_argument('birthday', type=str, help='birthday')
    def handle(self, *args, **kwargs):
        author = models.Author(
                name=kwargs.get('name'), 
                lastname=kwargs.get('lastname'),      
                email=kwargs.get('email'),
                biography=kwargs.get('biography'),
                birthday=kwargs.get('birthday'),
            )
        author.save()
        self.stdout.write(f'Author: {author}')