from .models import *


# 更新用户浏览记录
def update_user_browse(request):

    # 判断用户是否登录
    if not request.session.get('username', ''):
        return

    # 获得商品id和用户uid
    good_id = request.GET.get('id', '')
    user_id = request.session.get('uid', '')

    # 记录已存在,保存可以更新时间
    try:
        record = RecordBrowse.objects.get(browse_user_id=user_id, browse_goods_id=good_id)
        record.save()
    except RecordBrowse.DoesNotExist:
        records = RecordBrowse.objects.filter(browse_user_id=user_id).order_by('update_time')
        # 记录未满10条,直接新增一条记录
        if records.count() < 5:
            record = RecordBrowse()
            record.browse_goods_id = good_id
            record.browse_user_id = user_id
            record.save()
        # 记录超过10条,把时间最早的替换掉,也就是update_time最小的
        else:
            record = records[0]
            record.browse_goods_id = good_id
            record.save()






