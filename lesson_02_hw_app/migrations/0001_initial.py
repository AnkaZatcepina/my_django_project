# Generated by Django 4.2.5 on 2023-09-28 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.CharField(max_length=100)),
                ("registration_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=9)),
                ("quantity", models.IntegerField()),
                ("added_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cost", models.DecimalField(decimal_places=2, max_digits=9)),
                ("order_date", models.DateField(auto_now_add=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lesson_02_hw_app.client",
                    ),
                ),
                ("product", models.ManyToManyField(to="lesson_02_hw_app.product")),
            ],
        ),
    ]
