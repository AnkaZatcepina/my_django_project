# Generated by Django 4.2.5 on 2023-10-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lesson_02_hw_app", "0007_remove_product_image_name_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
