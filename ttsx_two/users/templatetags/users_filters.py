from django.template import Library
from django.core.urlresolvers import reverse

register = Library()


@register.filter
def create_menu(fl):

    menu = [
        {'link': reverse('users:centerinfo'), 'name': '个人信息', 'active': fl == 'info' and 'active' or ''},
        {'link': reverse('users:centerorder'), 'name': '全部订单', 'active': fl == 'order' and 'active' or ''},
        {'link': reverse('users:centersite'), 'name': '收货地址', 'active': fl == 'site' and 'active' or ''},
    ]

    return menu
# register.filter('create_menu', create_menu)


@register.filter
def record_sort(goods_list):

    # print(type(goods_list))
    my_goods = list()
    for goods in goods_list:
        my_goods.append(goods)

    # reverse=True, 逆向排序
    my_goods.sort(key=lambda obj: obj.update_time, reverse=True)

    return my_goods








