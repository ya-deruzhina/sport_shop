# Generated by Django 4.1 on 2024-08-10 14:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.IntegerField(default=0)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.categorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('date_of_pick_up', models.DateField()),
                ('time_of_pick_up', models.CharField(choices=[('9.00-10.00', '9.00-10.00'), ('10.00-11.00', '10.00-11.00'), ('11.00-12.00', '11.00-12.00'), ('12.00-13.00', '12.00-13.00'), ('13.00-14.00', '13.00-14.00'), ('14.00-15.00', '14.00-15.00'), ('15.00-16.00', '15.00-16.00'), ('16.00-17.00', '16.00-17.00'), ('17.00-18.00', '17.00-18.00')], max_length=100)),
                ('comment', models.TextField(default='Order without Comment', null=True)),
                ('total_money', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PickUpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=20, null=True)),
                ('id_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categorymodel')),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.CreateModel(
            name='RatingOfGoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('time_rating', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.goodsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('price_one', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ordermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.goodsmodel')),
            ],
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='pick_up_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.pickupmodel'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='goodsmodel',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='id_parent', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.subcategorymodel'),
        ),
        migrations.CreateModel(
            name='CommentOfGoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('time_comment', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.goodsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.goodsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
