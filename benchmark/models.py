from django.db import models

# Create your models here.
class BenchmarkCase(models.Model):
    case_name = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # input
    profile_model = models.FileField(upload_to='files/tmp/models/')
    profile_params = models.JSONField(null=True)
    # output
    profile_result = models.JSONField(null=True)
   
 
class HardwareDevice(models.Model):

    device_name = models.CharField(max_length=128)
    description = models.TextField()
    device_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_used = models.BooleanField(default=False)
    device_data = models.JSONField(null=True)