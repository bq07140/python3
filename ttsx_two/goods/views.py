from django.shortcuts import render
from .models import *
from .functions import *
from django.core.paginator import Paginator
from carts.models import Cart


# 三个页面要显示当前购物车数量,用装饰器完成
def cart_total_amount(func):
    def inner(request, *args, **kwargs):
        carts = Cart.objects.filter(cart_user_id=request.session.get('uid', ''))

        total = 0
        for cart in carts:
            total += cart.cart_amount
        request.total = total

        return func(request, *args, **kwargs)
    return inner


# 商品主页
@cart_total_amount
def index(request):

    ad1 = Advertise.objects.all()[:4]
    ad2 = Advertise.objects.all()[4:]

    # 获得商品所有分类
    cags = Category.objects.all()

    for cag in cags:

        # 4种最新的商品
        cag.new = Goods.objects.filter(goods_cag=cag).order_by('-id')[:4]
        # 3种热销商品
        cag.hot = Goods.objects.filter(goods_cag=cag).order_by('goods_sales')[:3]

    return render(request, 'goods/index.html', locals())


# 商品详细页
@cart_total_amount
def detail(request):

    # 根据跳转url中的id,得到商品
    g_id = request.GET.get('id', '').strip()
    # goods = Goods.objects.get(id=g_id)
    goods = Goods.objects.get(pk=g_id)

    # 获取最新的2个商品
    goods_new = Goods.objects.all().order_by('-id')[:2]

    # 更新用户浏览记录
    update_user_browse(request)

    return render(request, 'goods/detail.html', locals())


# 商品列表页
@cart_total_amount
def list(request, cag_id, page_id):

    # 获得商品分类
    cags = Category.objects.all()

    # 从url中获得参数show
    show = request.GET.get('show', '')

    # 根据分类获得商品列表
    if show == '':
        goods_list = Goods.objects.filter(goods_cag_id=cag_id)
    if show == 'price':
        goods_list = Goods.objects.filter(goods_cag_id=cag_id).order_by('-goods_price')
    if show == 'hot':
        goods_list = Goods.objects.filter(goods_cag_id=cag_id).order_by('-goods_price')

    # 创建分页对象
    paginator = Paginator(goods_list, 10)

    current_page = paginator.page(page_id)

    # 获取最新的2个商品
    goods_new = Goods.objects.all().order_by('-id')[:2]

    return render(request, 'goods/list.html', locals())



