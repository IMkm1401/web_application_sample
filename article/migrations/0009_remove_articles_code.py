# Generated by Django 4.1 on 2022-09-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_articles_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='code',
        ),
    ]