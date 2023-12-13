from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST
from .forms import BenchmarkCaseForm
# Create your views here.


@require_GET
def index(request):
    return render(request, 'index.html')



def create_benchmark_case(request):
    
    form = BenchmarkCaseForm(request.POST or None)
    
    return render(request, 'case_create.html',{"form":form})

@require_GET
def test_benchmark_case(request):
    return render(request, 'index.html')

@require_GET
def get_benchmark_cases(request):
    return render(request, 'index.html')

 

