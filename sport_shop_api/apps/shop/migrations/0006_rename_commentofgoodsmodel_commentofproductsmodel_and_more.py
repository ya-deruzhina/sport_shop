# Generated by Django 4.1 on 2024-08-17 19:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_alter_goodsmodel_subcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentOfGoodsModel',
            new_name='CommentOfProductsModel',
        ),
        migrations.RenameModel(
            old_name='GoodsModel',
            new_name='ProductsModel',
        ),
        migrations.RenameModel(
            old_name='RatingOfGoodsModel',
            new_name='RatingOfProductsModel',
        ),
    ]
