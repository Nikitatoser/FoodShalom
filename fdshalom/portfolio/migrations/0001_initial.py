# Generated by Django 5.0.2 on 2024-07-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="c",
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
                ("title", models.CharField(max_length=50, verbose_name="Назва")),
                ("full_text", models.TextField(verbose_name="Text")),
                (
                    "image_1",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "image_2",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "image_3",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "image_4",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "image_5",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
