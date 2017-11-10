from django.db import models
from db.base_model import *
from tinymce.models import HTMLField


# 分类模型
class Category(BaseModel):

    # 产品分类名称
    cag_name = models.CharField(max_length=30)


# 商品信息管理类
class GoodsManager(models.Manager):
    pass


# 商品模型
class Goods(BaseModel):

    # 商品名称
    goods_name = models.CharField(max_length=30)
    # 商品价格
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品的图片
    goods_image = models.ImageField()
    # 商品简述
    goods_short = models.CharField(max_length=100)
    # 商品详情
    goods_desc = HTMLField()
    # 商品上架
    goods_status = models.BooleanField(default=True)
    # 商品单位
    goods_unit = models.CharField(max_length=10)
    # 商品访问量
    goods_visit = models.IntegerField(default=0)
    # 商品销量
    goods_sales = models.IntegerField(default=0)
    # 商品分类
    goods_cag = models.ForeignKey(Category)

    objects = GoodsManager()


class Advertise(BaseModel):

    # 广告名称
    ad_name = models.CharField(max_length=30)
    # 广告图片
    ad_image = models.ImageField(upload_to='ad')
    # 广告链接
    ad_link = models.CharField(max_length=100)


# 详细商品页面, 浏览记录
class RecordBrowse(BaseModel):

    # 关联到goods应用下的Goods类
    browse_goods = models.ForeignKey('Goods')
    browse_user = models.ForeignKey('users.User')

