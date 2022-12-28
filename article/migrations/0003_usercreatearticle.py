# Generated by Django 4.1 on 2022-08-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articles_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreateArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='', upload_to='')),
            ],
        ),
    ]
