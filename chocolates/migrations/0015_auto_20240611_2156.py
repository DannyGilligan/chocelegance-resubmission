# Generated by Django 3.2.25 on 2024-06-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolates', '0014_alter_chocolate_choc_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolatereview',
            name='choc_rating',
            field=models.IntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name='chocolatereview',
            name='publish_review',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3, null=True),
        ),
    ]
