# Generated by Django 4.1 on 2022-09-22 12:22

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='message',
            field=models.TextField(default=builtins.print),
            preserve_default=False,
        ),
    ]
