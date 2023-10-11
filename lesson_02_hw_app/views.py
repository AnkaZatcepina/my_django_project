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


📌 Изменяем задачу с выводом двух html страниц:
главной и о себе.
📌 Перенесите вёрстку в шаблоны.
📌 Представления должны пробрасывать полезную информацию в
шаблон через контекст.
📌 Выделите общий код шаблонов и создайте родительский
шаблон base.html.


📌 Создайте шаблон, который выводит список заказанных
клиентом товаров из всех его заказов с сортировкой по
времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)
📌 *Товары в списке не должны повторятся.
"""
from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View
from . import models
from . import forms
import decimal
from datetime import datetime, timedelta
from django.template.response import TemplateResponse
from django.core.files.storage import FileSystemStorage

class MainView(View):
    def get(self, request):
        return render(request, "lesson_02_hw_app/index.html")

def about(request):
    return render(request, "lesson_02_hw_app/about.html")

def get_clients(request):
    clients = models.Client.objects.all()
    return HttpResponse(clients)

def get_products(request):
    products = models.Product.objects.all()
    return HttpResponse(products)

#lesson2/orders_by_client?client_id=3
#lesson2/orders_by_client/3
def get_orders_by_client(request, client_id: int):
    #client_id = request.GET.get('client_id')
    client = models.Client.objects.filter(pk=client_id)
    orders = models.Order.objects.filter(client__pk=client_id)
    context = {
        'client': client,
        'orders': orders
    }
    return render(request, "lesson_02_hw_app/orders_by_client.html", context) 
      

def create_order(request):
    client_id = request.GET.get('client_id')
    order = models.Order(client_id=client_id)
    order.save()
    return HttpResponse(order) 

#lesson2/add_product_to_order/?order_id=16&product_id=5
def add_product_to_order(request):
    order_id = request.GET.get('order_id')
    product_id = request.GET.get('product_id')
    order = models.Order.objects.filter(pk=order_id).first()
    product = models.Product.objects.filter(pk=product_id).first()  
    order_product = models.OrderProduct(order=order,
                                        product=product,
                                        quantity=1,
    )   
    order.products.add(product)
    order.save()
    return HttpResponse(order)        

def update_product_price(request, product_id: int, price: int):
    product = models.Product.objects.filter(pk=product_id).first()
    if product:
        product.price = price
        product.save()
        return HttpResponse('Цена товара изменена')
    else:
        return HttpResponse('Товар не найден')

def delete_order(request, order_id: int):
    order = models.Order.objects.filter(pk=order_id).first()
    if order:
        order.delete()
        return HttpResponse('Заказ удален')
    else:
        return HttpResponse('Заказ не найден')    

def filter_orders_min_date(request, client_id: int, min_date: datetime.date):
    client = models.Client.objects.filter(id=client_id).first()
    products = models.Product.objects.filter(orderproduct__order__client=client).distinct()
    if min_date == None:
        #orders = models.Order.objects.filter(client__pk=client_id).order_by('-order_date')
        pass 
    else:
        #orders = models.Order.objects.filter(client__pk=client_id,
        #                                   order_date__gte=min_date).order_by('-order_date') 
        products.filter(orderproduct__order__creating_date__gte=min_date)
            
    context = {
        'client': client,
        #'orders': orders,
        'products': products
    }
    #return render(request, "lesson_02_hw_app/products_by_client.html", context)  
    return render(request, "lesson_02_hw_app/products_by_client_new.html", context)                                        

def get_products_by_client(request, client_id: int):
    return filter_orders_min_date(request, client_id, None)      

def get_products_by_client_week(request, client_id: int):
    min_date = datetime.today() - timedelta(days=7)
    return filter_orders_min_date(request, client_id, min_date) 

def get_products_by_client_month(request, client_id: int):
    min_date = datetime.today() - timedelta(days=30)
    return filter_orders_min_date(request, client_id, min_date)      
    
def get_products_by_client_year(request, client_id: int):
    min_date = datetime.today() - timedelta(days=365)
    return filter_orders_min_date(request, client_id, min_date)    

def update_product(request, product_id: int):
    product = models.Product.objects.filter(pk=product_id).first()
    if product:
        if request.method == 'POST':
            form = forms.ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product.name = form.cleaned_data['name']
                product.description = form.cleaned_data['description']
                product.price = form.cleaned_data['price']
                product.quantity = form.cleaned_data['quantity']
                image = form.cleaned_data['image']
                #print('QQQQQQQQQQQQQ')
                #print(image)
                #fs = FileSystemStorage()
                #fs.save(image.name, image)
                product.image = image
                product.save()
        else:
            form = forms.ProductForm(initial={
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'quantity': product.quantity,
                'image': product.image,
            }) 
            #form = forms.ProductForm()
        return TemplateResponse(request, 'lesson_02_hw_app/update_product.html', context={'product': product, 'form': form})
        
    else:
        return HttpResponse('Товар не найден')