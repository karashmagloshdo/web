# Generated by Django 2.2.4 on 2020-03-17 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_marketingcallback_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscriber',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
