# Generated by Django 4.1 on 2022-09-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]