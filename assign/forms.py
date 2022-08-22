from django import forms
from django.forms import widgets
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from account.models import Profile

from account.models import LineToken

from assign.models import Assign, AssignProgress

#class LineTokenMultiple(forms.ModelMultipleChoiceField):
    #def label_form_instance(self, obj: LineToken) -> str:
        #return obj.name

class AssignModelChoice(forms.ModelChoiceField):
    def label_form_instance(self, obj):
        if obj.profile.rank:
            return obj.get_full_name()
        else:
            return obj.user.username

class AssignForm(forms.ModelForm):
    #images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'w3-input', 'multiple': True}), label="รูปภาพ", required=False)
    #tokens = LineTokenMultiple(
        #queryset=LineToken.objects.all(),
        #label="การแจ้งเตือน",
        #widget=widgets.CheckboxSelectMultiple(),
        #required=False
    #)
    assigned_to = AssignModelChoice(
            queryset=Profile.objects.all(),
            label='มอบงานหมายให้',
            #widget=widgets.Select(attrs={'class': 'form-control'})
            )

    class Meta:
        model   = Assign
        fields  = ('title', 'body', 'author', 'assigned_to',)
        widgets = {
                'title'       : widgets.TextInput(attrs   = {'class': 'w3-input'}),
                'body'        : widgets.Textarea(attrs    = {'class': 'form-control'}),
                # 'detail' : CKEditorWidget(attrs={'class': 'w3-input'}),
                #'assigned_to' : widgets.Select(attrs      = {'class': 'w3-select'}),
                'author'      : widgets.HiddenInput(attrs = {'class': 'w3-input', 'id': 'author'}),
                }
        labels = {
                'title'  : 'ชื่อเรื่อง',
                'body'   : 'รายละเอียด',
                'author' : 'ผู้เขียน',
                }

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ('status',)

        widgets = {
                'status' : widgets.Select(attrs={'class': 'form-control'}),
                #'note': widgets.Textarea(attrs={'class': 'form-control'}),
                }
        labels = {
                'status' : 'สถานะการดำเนินการ',
                }

class NoteForm(forms.ModelForm):
    class Meta:
        model = AssignProgress
        fields = ('note',)
