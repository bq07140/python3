from django.db import models
from db.base_model import BaseModel


# 购物车管理模型
class CartManager(models.Manager):
    pass


# 购物车模型
class Cart(BaseModel):
    cart_goods = models.ForeignKey('goods.Goods')
    cart_user = models.ForeignKey('users.User')
    cart_amount = models.IntegerField()

    objects = CartManager()

