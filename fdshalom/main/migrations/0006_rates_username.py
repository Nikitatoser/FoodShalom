# Generated by Django 5.0.2 on 2024-08-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_rates"),
    ]

    operations = [
        migrations.AddField(
            model_name="rates",
            name="username",
            field=models.CharField(
                default="Unknown", max_length=150, verbose_name="Username"
            ),
            preserve_default=False,
        ),
    ]
