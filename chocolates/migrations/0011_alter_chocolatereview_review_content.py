# Generated by Django 3.2.25 on 2024-06-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocolates', '0010_chocolatereview_publish_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolatereview',
            name='review_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
