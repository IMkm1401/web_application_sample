# Generated by Django 4.1 on 2022-09-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_userinformation_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user_email',
            field=models.TextField(),
        ),
    ]
