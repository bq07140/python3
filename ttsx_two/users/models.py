from django.db import models
from db.base_model import *


# 用户管理器
class UserManager(models.Manager):

    def user_by_name(self, username):
        try:
            return self.get(user_name=username)
        except User.DoesNotExist:
            return None


# # 基类创建
# class BaseModel(models.Model):
#
#     # 数据创建时间
#     create_time = models.DateTimeField(auto_now_add=True)
#     # 数据更新时间
#     update_time = models.DateTimeField(auto_now=True)
#     # 是否删除
#     is_delete = models.BooleanField(default=False)
#
#     # 抽象基类, 固定写法
#     class Meta:
#         abstract = True


# 建立用户模型
class User(BaseModel):

    # 用户名
    user_name = models.CharField(max_length=20)
    # 用户密码
    user_pass = models.CharField(max_length=64)
    # 用户联系电话
    user_tele = models.CharField(max_length=11)
    # 用户地址
    user_addr = models.CharField(max_length=100)
    # 用户邮箱
    user_mail = models.CharField(max_length=50)
    # 邮政编码
    user_code = models.CharField(max_length=10)
    # 收件人
    user_recv = models.CharField(max_length=20, default='')

    # 创建自定义管理器
    objects = UserManager()




