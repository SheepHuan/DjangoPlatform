from django.forms import ModelForm
from .models import BenchmarkCase
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
# https://juejin.cn/post/7128187234099920927

FRAMEWORK_TYPE=[
    (0,'Tensorflow Lite'),
    (1,'Paddle Lite'),
    (2,'Onnxrunime')
]

HARDWARE_DEVICE=[
    (0,'Android 0'),
    (1,'Android 1'),
    (2,'Android 3')
]

class BenchmarkCaseForm(ModelForm):
    framework_type = forms.ChoiceField(choices=FRAMEWORK_TYPE, label='Framework Type', initial=0)
    hardware_device = forms.ChoiceField(choices=HARDWARE_DEVICE, label='Hardware Device', initial=0)
    
    class Meta:
        model = BenchmarkCase
        fields = ('case_name',  'profile_model','description',)
        
        labels = {
            'case_name': 'Case Name',
            'description': 'Description',
            'profile_model': 'Profile Model',
            
        }
        
        widgets = {
            'case_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Case Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Case Description'}),
            'profile_model': forms.FileInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Profile Model'}),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'case_name',
            Row(
                Column('framework_type', css_class='form-group col-md-6 mb-0'),
                Column('hardware_device', css_class='form-group col-md-6 mb-0'),
            ),
            'profile_model',
            'description',
        )
