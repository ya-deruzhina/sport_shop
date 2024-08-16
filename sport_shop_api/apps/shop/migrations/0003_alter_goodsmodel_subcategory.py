# Generated by Django 4.1 on 2024-08-16 11:10

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_goodsmodel_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsmodel',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='id_parent', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategorymodel'),
        ),
    ]
