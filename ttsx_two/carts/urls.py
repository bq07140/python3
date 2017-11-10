from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^addcart/$', views.addcart, name='addcart'),
    url(r'^update_cart_data/$', views.update_cart_data, name='update_cart_data'),
]



