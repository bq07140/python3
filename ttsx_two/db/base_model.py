from django.db import models


# 基类创建
class BaseModel(models.Model):

    # 数据创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 数据更新时间
    update_time = models.DateTimeField(auto_now=True)
    # 是否删除
    is_delete = models.BooleanField(default=False)

    # 抽象基类, 固定写法
    class Meta:
        abstract = True



