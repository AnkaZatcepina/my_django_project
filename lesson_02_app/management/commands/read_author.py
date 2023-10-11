from django.core.management.base import BaseCommand
from ... import models

class Command(BaseCommand):
    help = "Read Author by ID"
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = models.Author.objects.filter(pk=pk).first()
        self.stdout.write(f'Author: {author}')