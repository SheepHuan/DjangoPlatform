from django.urls import path

from .views import index,create_benchmark_case,create_device


app_name = 'benchmark'


urlpatterns = [
    # 通过url函数设置url路由配置项
    path(r'', index,name="index"),
    path(r'add_case/', create_benchmark_case,name="add_benchmark_case"),
    path(r'add_device/', create_device,name="add_deivce"),
  
]

