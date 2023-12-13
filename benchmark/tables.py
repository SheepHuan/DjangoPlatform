import django_tables2 as tables
from .models import BenchmarkCase

class BenchmarkCaseTable(tables.Table):
    
    class Meta:
        model = BenchmarkCase
        template_name = "django_tables2/bootstrap5.html"