# Generated by Django 4.2.5 on 2023-09-28 12:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lesson_02_hw_app", "0002_rename_product_order_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="cost",
        ),
    ]
