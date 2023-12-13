from django.forms import ModelForm
from .models import BenchmarkCase, HardwareDevice
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

HARDWARE_DEVICE_TYPE = [
    (0,'Android'),
    (1,'Linux DevBorad'),
]

class HardwareDeviceForm(ModelForm):
    hardware_device_type = forms.ChoiceField(choices=HARDWARE_DEVICE_TYPE, label='Hardware Device Type', initial=1)
    address = forms.CharField(label='Address', max_length=128)
    ssh_username = forms.CharField(label='SSH Username', max_length=128)
    ssh_password = forms.CharField(label='SSH Password', max_length=128)
    class Meta:
        model = HardwareDevice
        fields = ('device_name','description' )
        
        labels = {
            'device_name': 'Device Name',  
            'description': 'Description',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['description'].required = False
        self.helper.layout = Layout(
            'device_name',   
            Row(
                Column('hardware_device_type', css_class='form-group col-md-6 mb-0'),
                Column('address', css_class='form-group col-md-6 mb-0'),
            ),
             Row(
                Column('ssh_username', css_class='form-group col-md-6 mb-0'),
                Column('ssh_password', css_class='form-group col-md-6 mb-0'),
            ),
            'description',
            Submit('submit', 'Submit', css_class='btn btn-primary'),
        )


class BenchmarkCaseForm(ModelForm):
    framework_type = forms.ChoiceField(choices=FRAMEWORK_TYPE, label='Framework Type', initial=0)
    hardware_device = forms.ChoiceField(choices=HARDWARE_DEVICE, label='Hardware Device', initial=0)
    
    class Meta:
        model = BenchmarkCase
        fields = ('case_name', 'profile_model','description',)
        
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
        self.fields['description'].required = False
        self.helper.layout = Layout(
            'case_name',
            Row(
                Column('framework_type', css_class='form-group col-md-6 mb-0'),
                Column('hardware_device', css_class='form-group col-md-6 mb-0'),
            ),
            'profile_model',
            'description',
            Submit('submit', 'Submit', css_class='btn btn-primary'),
        )
