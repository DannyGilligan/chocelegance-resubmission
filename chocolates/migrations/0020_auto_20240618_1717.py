# Generated by Django 3.2.25 on 2024-06-18 17:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolates', '0019_auto_20240617_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='choc_calories',
            field=models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='choc_carbs',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='choc_fat',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='choc_protein',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='chocolate',
            name='choc_sugar',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)]),
        ),
    ]