from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET,require_POST
from .forms import BenchmarkCaseForm,HardwareDeviceForm
from django_tables2 import RequestConfig
from .tables import BenchmarkCaseTable
from .models import BenchmarkCase
import os
@require_GET
def index(request):
    return render(request, 'case_table.html')

def create_case(request):
    form = BenchmarkCaseForm(request.POST or None)
    
    return render(request, 'case_create.html',{"form":form})



def create_device(request):
    if request.method == 'POST':
        print(request.POST)
        form = HardwareDeviceForm(request.POST)
    elif request.method == 'GET':
        form = HardwareDeviceForm(None)
    return render(request, 'device_create.html',{"form":form})




def get_case(request):
    from .models import FRAMEWORK_TYPE,FORWARD_TYPE
    def map_forward_type(forward_type):
        for i in FORWARD_TYPE:
            if i[0] == forward_type:
                return i[1]
    def map_framework_type(framework_type):
        for i in FRAMEWORK_TYPE:
            if i[0] == framework_type:
                return i[1]
    
    
    table = BenchmarkCase.objects.all()
    data_list = []
    for data_info in table:
        data_list.append({
            'case_name': data_info.case_name,
            'description': data_info.description,
            "created_at": data_info.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': data_info.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "profile_model": os.path.basename(data_info.profile_model.path),
            "device_name": data_info.device_name,
            "forward_type": map_forward_type(data_info.forward_type),
            "framework_type": map_framework_type(data_info.framework_type),
            "num_threads": data_info.num_threads,
            "num_warmup": data_info.num_warmup,
            "num_runs": data_info.num_runs,
            "latency": data_info.latency,
            "energy": data_info.energy,
        })
    data_dic = {}
    data_dic['data'] = data_list  #
    
    # return JsonResponse(data_dic)
    return HttpResponse(json.dumps(data_dic))

 

