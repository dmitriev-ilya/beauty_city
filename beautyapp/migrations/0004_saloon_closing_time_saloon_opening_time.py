# Generated by Django 4.1.7 on 2023-05-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0003_auto_20230524_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='saloon',
            name='closing_time',
            field=models.TimeField(default='20:00', verbose_name='время закрытия'),
        ),
        migrations.AddField(
            model_name='saloon',
            name='opening_time',
            field=models.TimeField(default='10:00', verbose_name='время открытия'),
        ),
    ]
