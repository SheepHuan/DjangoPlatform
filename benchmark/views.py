from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST
from .forms import BenchmarkCaseForm,HardwareDeviceForm
# Create your views here.


@require_GET
def index(request):
    return render(request, 'index.html')

def create_benchmark_case(request):
    form = BenchmarkCaseForm(request.POST or None)
    
    return render(request, 'case_create.html',{"form":form})


def create_device(request):
    if request.method == 'POST':
        print(request.POST)
        form = HardwareDeviceForm(request.POST)
    elif request.method == 'GET':
        form = HardwareDeviceForm(None)
        # print(form)
    return render(request, 'device_create.html',{"form":form})
 

