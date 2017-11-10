from django.core.urlresolvers import reverse
# from django.http import HttpResponse


# 记录用户最近一次访问的url
class RecordUrl(object):

    # 处理请求前
    def process_response(self, request, response):

        # 定义不记录的url列表
        exclue_urls = [
            reverse('users:login'),
            reverse('users:register'),
            reverse('users:login_handle'),
            reverse('users:register_handle'),
            reverse('users:centerinfo'),
            reverse('users:centersite'),
            reverse('users:centerorder'),
            reverse('users:logout'),
            '/favicon.ico',
        ]
        # print(request.path)
        # print(request.get_full_path())
        # print(response.status_code)
        # print('='*40)
        if request.path not in exclue_urls and response.status_code != '500':
            print('ggffffffffffffffffffffffffff')
            response.set_cookie('pre_url', request.get_full_path(), max_age=60*60*24)
        return response



