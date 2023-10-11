from django.contrib import admin
import decimal

"""
Задание №2
    📌 Подключите к админ панели созданные вами в рамках прошлых семинаров модели в приложении магазин

    📌 Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.
"""
from . import models


class ClientAdmin(admin.ModelAdmin):
    """Список Клиентов"""
    list_display = ['name', 'email', 'phone', 'registration_date']
    ordering = ['name', '-registration_date']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя(name)'

    """Отдельный Клиент"""
    readonly_fields = ['registration_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'registration_date'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'fields': ['email', 'phone', 'address'],
            },
        ),
    ]

@admin.action(description="Скидка 10")
def discount_10(modeladmin, request, queryset):
    for item in queryset:
        item.price*=decimal.Decimal(0.9)
        item.save()

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', 'price']
    list_per_page = 10
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя(name)'
    actions = [discount_10]

    readonly_fields = ['image_tag']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['image_tag', 'name', 'price'],
            },
        ),
        (
            'Подробно',
            {
                'classes': ['wide'],
                'fields': ['description', 'quantity'],
            },
        ),
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'order_date', 'cost']
    ordering = ['-order_date']
    list_filter = ['client']
    list_per_page = 10

    readonly_fields = ['cost']
    

admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderProduct)
