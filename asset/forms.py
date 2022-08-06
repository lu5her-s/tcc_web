from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

from asset.models import Asset

class DateInput(widgets.DateTimeBaseInput):
    input_type = 'date'
    format_key = 'DATE_INPUT_FORMATS'

class SelectAssignedAsset(widgets.Select):
    def label(self, obj):
        return obj.get_fullname()

class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ("name", "category", "model_no", 
                  "serial_no", "status", "manufacturer",
                  "supplier", "request_able", "purchase_date", 
                  "location_at", "assigned_to", 
                  "on_network", "note", "image",)
        labels = {
            "name" : "ชื่อ", 
            "model_no" : "โมเดล", 
            "serial_no" : "หมายเลขซีเรียล", 
            "purchase_date" : "จัดซื้อเมื่อ", 
            "assigned_to" : "มอบหมายให้", 
            "note" : "บันทึก", 
            "image" : "รูปภาพ", 
            "status" : "สถานะ", 
            "warranty_month" : "อายุรับประกัน/เดือน",
            "supplier" : "ผู้จัดจำหน่าย", 
            "request_able" : "การขอใช้งาน", 
            "location_at" : "สถานที่ที่สินทรัพย์อยู่",
            "manufacturer" : "ผู้ผลิต/ยี่ห้อ",
            # "quantity" : "จำนวน", 
            "on_network" : "เครือข่าย", 
            "category" : "ประเภท",
        }
        
        widgets = {
            "name" : widgets.TextInput(attrs={'class': 'w3-input',}), 
            "model_no" : widgets.Select(attrs={'class': 'w3-select',}),
            "serial_no" : widgets.TextInput(attrs={'class': 'w3-input', 'placeholder' : 'serial no.'}),
            "purchase_date" : DateInput(attrs={'class': 'w3-input',}),
            "assigned_to" : widgets.Select(attrs={'class': 'w3-select'}),
            # "assigned_to" : SelectAssignedAsset(attrs={'class': 'w3-select'}),
            "note" : widgets.Textarea(attrs={'class': 'w3-input'}),
            "image" : widgets.FileInput(attrs={'class': 'w3-input'}),
            "status" : widgets.Select(attrs={'class': 'w3-select'}),
            "warranty_month" : widgets.TextInput(attrs={'class': 'w3-input'}),
            "supplier" : widgets.Select(attrs={'class': 'w3-select'}),
            "request_able" : widgets.CheckboxInput(attrs={'class': 'w3-input w3-check', 'id': 'check'}), 
            "location_at" : widgets.Select(attrs={'class': 'w3-select'}),
            "manufacturer" : widgets.Select(attrs={'class': 'w3-select'}),
            # "quantity" : widgets.NumberInput(attrs={'class': 'w3-input', 'hidden': True}), 
            "on_network" : widgets.Select(attrs={'class': 'w3-select'}), 
            "category" : widgets.Select(attrs={'class': 'w3-select'}),
        }