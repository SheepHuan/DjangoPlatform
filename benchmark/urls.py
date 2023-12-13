from django.urls import path

from .views import index,create_case,create_device,get_case


app_name = 'benchmark'


urlpatterns = [
    # 通过url函数设置url路由配置项
    path(r'', index,name="index"),
    path(r'create_case/', create_case,name="create_case"),
    path(r'create_device/', create_device,name="create_deivce"),
    path(r'get_case/', get_case,name="get_case"),
]

