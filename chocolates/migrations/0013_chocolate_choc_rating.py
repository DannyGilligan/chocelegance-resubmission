# Generated by Django 3.2.25 on 2024-06-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolates', '0012_remove_chocolate_choc_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='chocolate',
            name='choc_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
