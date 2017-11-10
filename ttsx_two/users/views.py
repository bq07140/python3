from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import *
import re
import hashlib
from django.http import JsonResponse


# 用户注册页面
def register(request):

    return render(request, 'users/register.html', locals())


# 处理注册
def register_handle(request):

    user_name_input = request.POST.get('user_name', '').strip()
    user_pass1 = request.POST.get('user_pass1', '').strip()
    user_pass2 = request.POST.get('user_pass2', '').strip()
    user_mail_input = request.POST.get('user_mail', '').strip()
    mess = {}
    # 定义函数判断输入是否合法
    def check_register():

        flag = True

        if (not(5<=len(user_name_input)<=20)):
            mess['user_name'] = '请检查用户名长度,保证在5-20个字符之间!'
            flag = False
            return flag

        # 检验用户名是否已经注册过了
        try:
            User.objects.get(user_name=user_name_input)
            mess['user_name'] = '用户名已注册,请重新输入!'
            flag = False
            return flag
        except User.DoesNotExist:
            pass

        if (not(8<=len(user_pass1)<=20)):
            mess['user_pass1'] = '请检查密码长度,保证在8-20个字符之间!'
            flag = False
            return flag
        if (user_pass1 != user_pass2):
            mess['user_pass2'] = '两次输入的密码不相同,请重新输入!'
            flag = False
            return flag

        reg = '^[a-z0-9][\w\.\-]*@[a-z0-9]+(\.[a-z]{2,5}){1,2}$'
        if not re.match(reg, user_mail_input):
            mess['user_mail'] = '您输入的邮箱不存在!'
            flag = False
            return flag

        # 检验邮箱是否已经注册过了
        try:
            users = User.objects.get(user_mail=user_mail_input)
            mess['user_mail'] = '邮箱已注册,请重新输入!'
            flag = False
            return flag
        except User.DoesNotExist:
            pass
        return flag

    # 判断输入是否合法
    if check_register():
        # 1.1 输入合法,保存到数据库
        user = User()
        user.user_name = user_name_input

        # 密码需要加密后再存储到数据库
        sha = hashlib.sha256()
        # 前后加符号后再加密,
        pass_word = 'djkfjddk' + user_pass1 + 'jfkdjfdk'
        sha.update(pass_word.encode('utf-8'))
        user.user_pass = sha.hexdigest()

        user.user_mail = user_mail_input
        user.save()
        return render(request, 'users/login.html', locals())
    else:
        # 1.2 不合法,跳转到注册页面
        return render(request, 'users/register.html', locals())


# 注册时, ajax 检测用户名是否存在
def check_username(request):

    # 从register.js中获得参数
    user_name_input2 = request.GET.get('username', '').strip()
    print(user_name_input2, 'aaaaaaaaaaaaaaaaaaaa')

    if User.objects.get(user_name=user_name_input2):
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({'ret': 0})


# 注册时, ajax 检测用户邮箱是否存在
def check_usermail(request):

    # 从register.js中获得参数
    user_mail_input2 = request.GET.get('usermail', '').strip()
    print(user_mail_input2, 'bbbbbbbbbbbbbbbbbbbbb')

    if User.objects.get(user_mail=user_mail_input2):
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({'ret': 0})


# 用户登录
def login(request):

    return render(request, 'users/login.html', locals())


# 处理登录
def login_handle(request):

    user_name_login = request.POST.get('username', '').strip()
    user_pwd_login = request.POST.get('pwd', '').strip()

    user = User.objects.user_by_name(user_name_login)

    # 检测登录参数
    def check_login_params():

        flag = True
        if (not(5<=len(user_name_login)<=20)):
            flag = False
            return flag

        if (not(8<=len(user_pwd_login)<=20)):
            flag = False
            return flag

        if user:
            # 密码需要加密后再存储到数据库
            sha = hashlib.sha256()
            # 前后加符号后再加密,
            pass_word2 = 'djkfjddk' + user_pwd_login + 'jfkdjfdk'
            sha.update(pass_word2.encode('utf-8'))
            pass_word2 = sha.hexdigest()

            if pass_word2 == user.user_pass:
                return flag
            else:
                flag = False
                return flag
        else:
            flag = False
            return flag

        return flag

    if check_login_params():

        # 1.记录用户状态
        request.session['username'] = user_name_login
        request.session['uid'] = user.id

        # 2.是否需要记录用户名, 设置cookie
        remember = request.POST.get('user_memb', '').strip()

        if remember:
            HttpResponse.set_cookie('username', user_name_login, max_age=60*60*24)

        # 3.获得跳转 url
        url = request.COOKIES.get('pre_url', '')
        if not url:
            url = reverse('goods:index')
        return redirect(url)

    else:
        return render(request, 'users/login.html')


# 退出登录
def logout(request):

    # 1.保存最近一次 url
    url = request.COOKIES.get('pre_url', '').strip()
    if not url:
        url = reverse('goods:index')

    # 2.清空session
    request.session.flush()

    return redirect(url)


# 装饰器,检查用户是否登录
def view_premission(func):
    def wrapper(request, *args, **kwargs):
        
        if request.session.get('username', ''):
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('users:login'))
    return wrapper


# 用户中心
@view_premission
def centerinfo(request):

    user = User.objects.get(user_name=request.session.get('username', ''))

    return render(request, 'users/user_center_info.html', locals())


# 处理收件人信息
def recv_message_handle(request):

    user_recv = request.POST.get('user_recv', '')
    user_addr = request.POST.get('user_addr', '')
    user_code = request.POST.get('user_code', '')
    user_tele = request.POST.get('user_tele', '')

    if len(user_recv) != 0 and len(user_addr) != 0 and len(user_code) == 6 and len(user_tele) == 11:
        user = User.objects.get(user_name=request.session.get('username', ''))
        user.user_recv = user_recv
        user.user_addr = user_addr
        user.user_code = user_code
        user.user_tele = user_tele
        user.save()

    return redirect(reverse('users:centersite'))


# 用户订单
@view_premission
def centerorder(request):

    return render(request, 'users/user_center_order.html', locals())


# 用户地址
@view_premission
def centersite(request):

    user = User.objects.get(user_name=request.session.get('username', ''))
    return render(request, 'users/user_center_site.html', locals())

