# Generated by Django 4.1 on 2024-07-10 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_ratingofgoodsmodel_time_r_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingofgoodsmodel',
            name='time_rating',
        ),
    ]
