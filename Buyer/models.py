from django.db import models

# Create your models here.
# 买家模型类
class Buyer(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(max_length=32,verbose_name="联系电话",null=True,blank=True)
    connect_address = models.TextField(verbose_name="联系地址",null=True,blank=True)

    class Meta:
        verbose_name = "买家"
        verbose_name_plural = "买家"


# 地址
class Address(models.Model):
    address = models.TextField(verbose_name="收货地址")
    recver = models.CharField(max_length=32,verbose_name="接收人")
    recv_phone = models.CharField(max_length=32,verbose_name="收件人电话")
    post_number = models.CharField(max_length=32,verbose_name="邮编")
    buyer_id = models.ForeignKey(to=Buyer,on_delete=models.CASCADE,verbose_name="用户id")

    class Meta:
        verbose_name = "地址"
        verbose_name_plural = "地址"

# v3.5 订单
class Order(models.Model):
    order_id = models.CharField(max_length=32,verbose_name="订单编号")
    goods_count = models.IntegerField(verbose_name="商品数量")
    order_user = models.ForeignKey(to=Buyer,on_delete=models.CASCADE,verbose_name="订单用户")
    order_address = models.ForeignKey(to=Address,on_delete=models.CASCADE,verbose_name="订单地址",blank=True,null=True)
    order_price = models.FloatField(verbose_name="订单总价")
    # v3.7 添加订单状态：未支付1；待发货2；已发货3；已收货4；已退货0
    order_status = models.IntegerField(default=1,verbose_name="订单状态")

# v3.5 订单详情
class OrderDetail(models.Model):
    order_id = models.ForeignKey(to=Order,on_delete=models.CASCADE,verbose_name="订单编号")
    goods_id = models.IntegerField(verbose_name="商品id")
    goods_name = models.CharField(max_length=32,verbose_name="商品名称")
    goods_price = models.FloatField(verbose_name="商品价格")
    goods_number = models.IntegerField(verbose_name="商品购买数量")
    goods_total = models.FloatField(verbose_name="商品总价")
    goods_store = models.IntegerField(verbose_name="店铺id")
    goods_image = models.ImageField(verbose_name="商品图片")

# v3.8 购物车
class Cart(models.Model):
    goods_name = models.CharField(max_length=32,verbose_name="商品名称")
    goods_price = models.FloatField(verbose_name="商品价格")
    goods_total = models.FloatField(verbose_name="单类商品总价")
    goods_number = models.IntegerField(verbose_name="商品数量")
    goods_picture = models.ImageField(upload_to="buyer/images",verbose_name="商品图片")
    goods_id = models.IntegerField(verbose_name="商品id")
    goods_store = models.IntegerField(verbose_name="商品店铺")
    user_id = models.IntegerField(verbose_name="用户id")
