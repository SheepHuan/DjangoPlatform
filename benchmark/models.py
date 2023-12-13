from django.db import models

HARDWARE_DEVICE_TYPE = [
    (0,'Android'),
    (1,'Linux DevBorad'),
]

FRAMEWORK_TYPE=[
    (0,'Tensorflow Lite'),
    (1,'Paddle Lite'),
    (2,'Onnxrunime')
]

FORWARD_TYPE=[
    (0,'cpu'),
    (1,'gpu'),
    (2,'npu'),
    (3,'dsp')
]

# Create your models here.
class BenchmarkCase(models.Model):
    case_name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # input
    profile_model = models.FileField(upload_to='files/tmp/models/')
    
    device_name = models.CharField(max_length=128)
    # 
    framework_type = models.IntegerField(default=0)
    # 
    forward_type = models.IntegerField(default=0)
    # 
    num_threads = models.IntegerField(default=4)
    num_warmup = models.IntegerField(default=10)
    num_runs = models.IntegerField(default=50)
    
    latency = models.FloatField(null=True,blank=True)
    energy = models.FloatField(null=True,blank=True)
 
class HardwareDevice(models.Model):

    device_name = models.CharField(max_length=128)
    description = models.TextField()
    device_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_used = models.BooleanField(default=False)
    device_data = models.JSONField(null=True)