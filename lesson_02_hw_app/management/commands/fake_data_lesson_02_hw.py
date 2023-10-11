from django.core.management.base import BaseCommand
from ... import models
import random
import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    random_time = start + datetime.timedelta(seconds=random_second)
    return random_time.date()

class Command(BaseCommand):
    help = "Generate fake clients, products and orders"
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='amount')
    def handle(self, *args, **kwargs):
        d1 = datetime.datetime.strptime('1/1/2022 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.datetime.now()

        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = models.Client(
                name=f'Client{i}', 
                email=f'mail{i}@mail.ru',
                phone=f'+7(908)00{i}',
                address=f'Street, Home {i}',
            )
            client.save()
            product = models.Product(
                name=f'Product{i}', 
                description=f'Descr{i}',
                price=100*i,
                quantity=10+i,
            )
            product.save()
        clients = models.Client.objects.all()
        products = models.Product.objects.all()

        for _ in range(count * 20):
            random_client = models.Client.objects.order_by('?')[0]
            random_date_1=random_date(d1, d2)
            order = models.Order(
                client=random_client,  
                order_date=random_date_1,              
            )
            order.save()
            for j in range(3):
                #random_product = models.Product.objects.order_by('?')[0]            
                #order.products.add(random_product)
            #order.save()
                random_product = models.Product.objects.order_by('?')[0]
                order_product = models.OrderProduct(
                    order=order,  
                    product=random_product,
                    quantity=j,        
                )
                order_product.save()
        