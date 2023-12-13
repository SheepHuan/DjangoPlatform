from django.contrib import admin
from .models import BenchmarkCase,HardwareDevice
# Register your models here.
admin.site.register(BenchmarkCase)
admin.site.register(HardwareDevice)