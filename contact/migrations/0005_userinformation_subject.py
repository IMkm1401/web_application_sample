# Generated by Django 4.1 on 2022-09-22 12:55

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_userinformation_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='subject',
            field=models.CharField(default=builtins.print, max_length=100),
            preserve_default=False,
        ),
    ]
