# Generated by Django 4.1 on 2024-07-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_commentofgoodsmodel_t_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentofgoodsmodel',
            name='time',
        ),
        migrations.AddField(
            model_name='ratingofgoodsmodel',
            name='t_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
