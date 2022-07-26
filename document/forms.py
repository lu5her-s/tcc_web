from django import forms
from django.forms import widgets
from django.contrib.auth.models import Group, User

from document.models import Inbox, Outbox
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

class OutboxForm(forms.ModelForm):
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
        model = Outbox
        fields = ('out_no', 'out_from', 'send_to', 'send_out', 'doc_no', 'urgency', 'title', 'doc_date', 'ref_doc', 'sender',)
        widgets = {
                'out_no':   widgets.TextInput(attrs={'class': 'form-control'}),
                'out_from': widgets.Select(attrs={'class': 'form-control'}),
                'send_to':  widgets.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
                'send_out': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'นอกหน่วย นขต.กทข.ศทส.สส.'}),
                'doc_no':   widgets.TextInput(attrs={'class': 'form-control'}),
                'urgency':  widgets.Select(attrs={'class': 'form-control'}),
                'title':    widgets.TextInput(attrs={'class': 'form-control'}),
                'doc_date': DateInput(),
                'ref_doc':  widgets.Select(attrs={'class': 'form-control'}),
                'sender':   widgets.HiddenInput(attrs={'class': 'form-control', 'id': 'sender'}),
                }
        labels = {
                'out_no': 'เลขออกที่',
                'out_from': 'จาก',
                'send_to': 'ถึง',
                'send_out':'ส่งนอกหน่วย นขต.',
                'doc_no':'เอกสารเลขที่',
                'urgency':'ความเร่งด่วน',
                'title':'เรื่อง',
                'doc_date':'ลงวันที่',
                'ref_doc':'อ้างถึง',
                }
