from django.urls import path
from Buyer.views import *
# v2.6 新建buyer app 的独立url
urlpatterns = [
    path('login/', login), # 前台登录
    path('register/', register), # 前台注册
    path('logout/', logout), # 前台退出
    path('index/', index), # 前台首页
    path('goods_list/', goods_list), # 前台商品列表页
    path('pay_order/', pay_order), # v3.3 前台商品支付页面
    path('pay_result/', pay_result), # v3.3 前台商品支付结束响应页面
    path('goods_detail/', goods_detail), # v3.4 前台商品详情页
    path('place_order/', place_order), # v3.5 订单详情页
    path('cart/', cart), # v3.8 购物车列表
    path('add_cart/', add_cart), # v3.8 添加购物车
    path('del_cart/', del_cart_goods), # v4.1 删除购物车

]

urlpatterns += [
    path('base/', base),

]