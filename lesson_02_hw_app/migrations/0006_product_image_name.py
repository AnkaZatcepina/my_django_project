# Generated by Django 4.2.5 on 2023-10-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "lesson_02_hw_app",
            "0005_remove_order_products_alter_order_order_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image_name",
            field=models.ImageField(
                blank=True, default="empty.jpg", upload_to="", verbose_name="Product_"
            ),
        ),
    ]