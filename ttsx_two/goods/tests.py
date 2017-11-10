from django.test import TestCase
from .models import *
import random


cags = ['新鲜水果', '海鲜水产', '猪牛羊肉', '禽类蛋品', '新鲜蔬菜', '速冻食品']

# for cag in cags:
#     c = Category()
#     c.cag_name = cag
#     c.save()
#
# units = ['500克', '20毫升', '1条', '3包', '1支', '1套', '1部', '1台']
#
# # 创建商品测试数据
# try:
#     f = open('/home/python/Desktop/6.项目进级/ttsx_two/data.txt', 'r')
#     print(f)
#     for line in f:
#         # 创建商品对象
#         print(11111)
#         g = Goods()
#         g.goods_name = line[:-1]
#         g.goods_short = '真材实料, 百年品质'
#         g.goods_desc = '商0万-15量：4000mAh-5999mAh机身内存'
#         g.goods_cag_id = random.randint(1, len(cags))
#         g.goods_image = 'goods/' + str(random.randint(1, 18)) + '.jpg'
#         g.goods_price = random.randint(1, 999)
#         g.goods_unit = units[random.randint(0, len(units)-1)]
#         g.save()
# except Exception as e:
#     print(e)


# 创建广告数据
for index in range(1, 5):
    ad1 = Advertise()
    ad1.ad_name = '广告1'
    ad1.ad_image = 'goods/ad/slide0' + str(index) + '.jpg'
    ad1.ad_link = '#'
    ad1.save()

for index in range(1, 3):
    ad2 = Advertise()
    ad2.ad_name = '广告2'
    ad2.ad_image = 'goods/ad/adv0' + str(index) + '.jpg'
    ad2.ad_link = '#'
    ad2.save()



