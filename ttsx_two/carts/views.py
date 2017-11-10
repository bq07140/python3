from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *


# 我的购物车页面
def index(request):

    carts = Cart.objects.filter(cart_user_id=request.session.get('uid', ''))

    money = 0
    total = 0
    for cart in carts:

        cart.total = cart.cart_goods.goods_price*cart.cart_amount
        money += cart.total
        total += cart.cart_amount

    return render(request, 'carts/cart.html', locals())


# 点击加入购物车时, 数据存储到数据库
def addcart(request):

    goods_id = request.GET.get('goods_id', '').strip()
    goods_num = request.GET.get('goods_num', '').strip()
    user_id = request.session.get('uid', '')

    # 如果存在,则更新数量
    try:
        cart = Cart.objects.get(cart_user_id=user_id, cart_goods_id=goods_id)
        cart.cart_amount = cart.cart_amount + int(goods_num)
        cart.save()
        # cart = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        # cart.cart_amount = cart.cart_amount + int(goods_num)
        # cart.save()
    except Cart.DoesNotExist:
        cart = Cart()
        cart.cart_goods_id = goods_id
        cart.cart_amount = goods_num
        cart.cart_user_id = user_id
        cart.save()

    # 更新购物车总数量
    carts = Cart.objects.filter(cart_user_id=user_id)
    total = 0
    for cart in carts:
        total = cart.cart_amount
    return JsonResponse({'total': total})


# 我的购物车中, 修改数量等数据, 数据库联动
def update_cart_data(request):

    goods_id = request.GET.get('goods_id', '')
    goods_num = request.GET.get('goods_num', '')

    try:
        cart = Cart.objects.get(cart_user_id=request.session.get('uid', ''), cart_goods_id=goods_id)
        cart.cart_goods_id = goods_id
        cart.cart_amount = goods_num
        cart.save()
    except Cart.DoesNotExist:
        return JsonResponse({'ret': 0})
    return JsonResponse({'ret': 1})

