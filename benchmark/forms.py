from django.forms import ModelForm
from .models import BenchmarkCase, HardwareDevice
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import HARDWARE_DEVICE_TYPE,FRAMEWORK_TYPE
# https://juejin.cn/post/7128187234099920927



HARDWARE_DEVICE=[
    (0,'Android 0'),
    (1,'Android 1'),
    (2,'Android 3')
]



class HardwareDeviceForm(ModelForm):
    hardware_device_type = forms.ChoiceField(choices=HARDWARE_DEVICE_TYPE, label='Hardware Device Type', initial=1)
    address = forms.CharField(label='Address', max_length=128)
    ssh_username = forms.CharField(label='SSH Username', max_length=128,required=False)
    ssh_password = forms.CharField(label='SSH Password', max_length=128,required=False)
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

    def clean_ssh_username(self):
        ssh_username = self.cleaned_data['ssh_username']
        if not ssh_username and self.cleaned_data['hardware_device_type'] == 1:
            raise forms.ValidationError('SSH Username is required')
        return ssh_username

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
