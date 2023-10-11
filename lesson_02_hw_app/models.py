"""
Создайте три модели Django: клиент, товар и заказ.

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
    — имя клиента
    — электронная почта клиента
    — номер телефона клиента
    — адрес клиента
    — дата регистрации клиента

Поля модели «Товар»:
    — название товара
    — описание товара
    — цена товара
    — количество товара
    — дата добавления товара

Поля модели «Заказ»:
    — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
    — связь с моделью «Товар», указывает на товары, входящие в заказ
    — общая сумма заказа
    — дата оформления заказа

Допишите несколько функций CRUD для работы с моделями по желанию. 
"""

from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

class Client(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}, {self.email}'

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="/static/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    def __str__(self):
        return f'{self.name}, {self.price}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #products = models.ManyToManyField(Product)
    order_date = models.DateField(default=timezone.now().date())

    def cost(self):
        #summ = self.products.all().aggregate(models.Sum('price'))
        summ = 0
        for item in self.orderproduct_set.all():
            p = Product.objects.filter(pk=item.product_id).first()
            if not p:
                continue
            p = p.price
            summ += item.quantity * p
        return summ

    """def __str__(self):
        products = self.products.all()
        result = f'ID: {self.pk} Client: {self.client}, Cost: {self.cost()}, \n Products: \n'
        for product in list(products):
           result += f'{str(product)}\n'

        return result"""


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()