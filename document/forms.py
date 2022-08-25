from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

from document.models import Inbox

class DateInput(widgets.DateTimeBaseInput):
    input_type = 'date'
    #format_key = 'DATETIME_INPUT_FORMATS' 
    format_key = 'DATE_INPUT_FORMATS'

class InboxForm(forms.ModelForm):
    files = forms.FileField(
            widget=widgets.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'multiple': True,
                    }
                ),
            label='ไฟล์เอกสาร'
            )
    class Meta:
        model = Inbox
        fields = ('receive_no', 'send_from', 'doc_no', 'urgency', 'title', 'doc_type', 'doc_date', 'receiver', 'status', 'files')
        widgets = {
                'receive_no' : widgets.TextInput(attrs={'class' : 'form-control'}),
                'send_from' : widgets.TextInput(attrs={'class' : 'form-control'}),
                'doc_no' : widgets.TextInput(attrs={'class' : 'form-control'}),
                'urgency' : widgets.Select(attrs={'class': 'form-control'}),
                'title' : widgets.TextInput(attrs={'class': 'form-control'}),
                'doc_type' : widgets.Select(attrs={'class' : 'form-control'}),
                'doc_date' : DateInput(),
                'receiver' : widgets.HiddenInput(attrs={'class': 'form-control', 'id': 'receiver'}),
                'status' : widgets.Select(attrs={'class': 'form-control'}),
                }
        labels = {
                'receive_no': 'เลขรับที่',
                'send_from': 'จาก',
                'doc_no' : 'เลขที่เอกสาร',
                'urgency' : 'ความเร่งด่วน',
                'title' : 'เรื่อง',
                'doc_type': 'ประเภท',
                'doc_date' : 'ลงวันที่',
                'status' : 'สถานะ', 
                }
