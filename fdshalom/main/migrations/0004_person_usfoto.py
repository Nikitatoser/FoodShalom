# Generated by Django 5.0.2 on 2024-08-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="usfoto",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
