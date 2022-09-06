from django import forms
from django.forms import widgets
from django.contrib.auth.models import Group, User

from account.models import Profile
from document.models import Document

class DateInput(widgets.DateTimeBaseInput):
    input_type = 'date'
    #format_key = 'DATETIME_INPUT_FORMATS' 
    format_key = 'DATE_INPUT_FORMATS'

class DocumentForm(forms.ModelForm):
    class Meta:
        model   = Document
        fields  = ('document_no', 'urgency', 'title', 'assigned_to', 'assigned_group', 'document_file', 'author',)
        widgets = {
                'document_no':    widgets.TextInput(attrs={'class':              'form-control'}),
                'urgency':        widgets.Select(attrs={'class':                 'form-control'}),
                'title':          widgets.TextInput(attrs={'class':              'form-control'}),
                'assigned_to':    widgets.Select(attrs={'class': 'form-control'}),
                'assigned_group': widgets.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
                'document_file':  widgets.FileInput(attrs={'class':              'form-control'}),
                'author':         widgets.HiddenInput(attrs={'class':            'form-control', 'id': 'author'}),
                }
