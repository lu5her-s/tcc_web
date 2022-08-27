from django import forms
from django.forms import widgets
from django.contrib.auth.models import Group, User

from document.models import Inbox
from account.models import Profile

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
    #assigned_to = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple(), label='ผู้รับปฏิบัติ')
    #assigned_group = forms.ModelMultipleChoiceField(queryset=None, widget=forms.CheckboxSelectMultiple(), label='แผนกที่เกี่ยวข้อง')

    class Meta:
        model = Inbox
        fields = ('receive_no', 'send_from', 'doc_no', 'urgency', 'title', 'doc_type', 'doc_date', 'receiver', 'status', 'assigned_to', 'assigned_group', 'files')
        widgets = {
                'receive_no' : widgets.TextInput(attrs={'class' : 'form-control'}),
                'send_from' : widgets.TextInput(attrs={'class' : 'form-control'}),
                'doc_no' : widgets.TextInput(attrs={'class' : 'form-control'}),
                'urgency' : widgets.Select(attrs={'class': 'form-control'}),
                'title' : widgets.TextInput(attrs={'class': 'form-control'}),
                'doc_type' : widgets.Select(attrs={'class' : 'form-control'}),
                'doc_date' : DateInput(),
                'receiver' : widgets.HiddenInput(attrs={'class': 'form-control', 'id': 'receiver'}),
                'assigned_to': widgets.Select(attrs={'class': 'form-control'}),
                #'assigned_to': forms.ModelMultipleChoiceField(queryset=None),
                'assigned_group':widgets.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
                #'assigned_group': forms.ModelMultipleChoiceField(queryset=None),
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
                'assigned_to': 'ผู้รับดำเนินการ',
                'assigned_group': 'แผนกที่เกี่ยวข้อง',
                'status' : 'สถานะ', 
                }

        # def __init__(self, *args, **kwargs):
            # super().__init__(*args, **kwargs)
            # self.fields['assigned_to'].queryset = Profile.objects.all()
            # self.fields['assigned_group'].queryset = Group.objects.all()
