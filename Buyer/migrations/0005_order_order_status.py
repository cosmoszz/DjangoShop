# Generated by Django 2.1.1 on 2019-07-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0004_orderdetail_goods_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(default=1, verbose_name='订单状态'),
        ),
    ]
