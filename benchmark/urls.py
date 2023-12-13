from django.urls import path

from .views import index,create_benchmark_case


app_name = 'benchmark'


urlpatterns = [
    # 通过url函数设置url路由配置项
    path(r'', index,name="index"),
    path(r'create/', create_benchmark_case,name="create_benchmark_case"),
]

