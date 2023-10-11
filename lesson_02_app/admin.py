from django.contrib import admin
"""
Задание №2
    📌 Подключите к админ панели созданные вами в рамках прошлых семинаров модели в приложениях:
    ○ случайные числа
    ○ блог
Задание №5
    📌 Настройте под свои нужды вывод информации об авторах, статьях и комментариях на страницах списков.    
"""
from . import models
# Register your models here.

@admin.action(description="Очистить биографию")
def reset_bio(modeladmin, request, queryset):
    queryset.update(biography='')

class AuthorAdmin(admin.ModelAdmin):
    """Список Авторов"""
    list_display = ['name', 'lastname', 'birthday']
    ordering = ['name', '-lastname']
    list_filter = ['name']
    list_per_page = 4
    search_fields = ['lastname']
    search_help_text = 'Поиск по полю Фамилия(lastname)'
    actions = [reset_bio]

    """Отдельный Автор"""
    readonly_fields = ['birthday']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'lastname'],
            },
        ),
        (
            'Био',
            {
                'classes': ['collapse'],
                'description': 'Био автора',
                'fields': ['birthday', 'biography'],
            },
        ),
            (
            'Контакты',
            {
                'fields': ['email'],
            }
        ),
    ]
admin.site.register(models.Coin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Article)
admin.site.register(models.Comment)