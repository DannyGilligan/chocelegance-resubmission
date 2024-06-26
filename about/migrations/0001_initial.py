# Generated by Django 3.2.25 on 2024-06-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_question', models.CharField(max_length=500)),
                ('faq_answer', models.TextField()),
                ('faq_publish', models.CharField(choices=[('Yes', 'Yes'), ('No', 'Yes')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
