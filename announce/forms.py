from django import forms
from django.forms import widgets

from account.models import LineToken

from .models import Announce, Comment

class LineTokenMultiple(forms.ModelMultipleChoiceField):
    def label_form_instance(self, obj: LineToken) -> str:
        return obj.name
    
class AnnounceForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'w3-input', 'multiple' : True}), label="เอกสารที่เกี่ยวข้อง")
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'w3-input', 'multiple': True}), label="รูปภาพ")
    token = LineTokenMultiple(
        queryset=LineToken.objects.all(),
        label="การแจ้งเตือน",
        widget=widgets.CheckboxSelectMultiple(attrs={'class': 'w3-check'})
    )
    
    class Meta:
        model = Announce
        fields = ('is_type', 'name', 'detail', 'status', 'author', 'images', 'files', 'token',)
        widgets = {
            'is_type' : widgets.Select(attrs={'class': 'w3-select'}),
            'name' : widgets.TextInput(attrs={'class': 'w3-input'}),
            'detail' : widgets.Textarea(attrs={'class': 'w3-input'}),
            'status' : widgets.Select(attrs={'class': 'w3-select'}),
            'author' : widgets.HiddenInput(attrs={'class': 'w3-input', 'id': 'author'}),
        }
        labels = {
            'is_type' : 'ประเภท', 
            'name' : 'ชื่อเรื่อง',
            'detail' : 'รายละเอียด',
            'status' : 'สถานะ',
            'author' : 'ผู้เขียน',
            'token' : 'การแจ้งเตือน',
        }
