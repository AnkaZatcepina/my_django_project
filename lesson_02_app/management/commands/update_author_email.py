from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    help = "Update Author by ID"
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('email', type=str, help='email')
       
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        email = kwargs.get('email')
        author = models.Author.objects.filter(pk=pk).first()
        author.email = email
        author.save()
        self.stdout.write(f'Author: {author}')