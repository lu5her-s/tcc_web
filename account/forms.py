from cProfile import label
from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from account.models import Sector, Rank, Position, Profile, LineToken

class SectorChoiceField(forms.ModelChoiceField):
    def label_form_instance(self, obj):
        return obj.name

class RankChoiceField(forms.ModelChoiceField):
    def label_form_instance(self, obj):
        return obj.name
    
class PositionChoiceField(forms.ModelChoiceField):
    def label_form_instance(self, obj):
        return obj.name

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username' : 'ชื่อสำหรับเข้าใช้งาน',
            'email' : 'อีเมลล์',
            # 'password1' : 'รหัสผ่าน',
            # 'password2' : 'ยืนยันรหัสผ่าน'
		}
        # help_text = {
		# 	'username' : 'ตัวอักษรภาษาอังกฤษ',
		# 	'password1' : 'รหัสผ่านสำหรับเข้าสู่ระบบ ประกอบด้วยอย่างน้อย 8 ตัว',
		# 	'password2' : 'ใส่รหัสผ่านเดียวกันกับด้านบนเพื่อยืนยัน'
		# }
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "รหัสผ่าน"
        self.fields['password2'].label = "ยืนยันรหัสผ่าน"
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email'
        )
        labels = {
            'first_name': 'ชื่อ',
            'last_name': 'นามสกุล',
            'email': 'Email'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'input w3-input'}),
            'email' : forms.EmailInput(attrs={'class': 'input w3-input'})
        }

class ProfileForm(forms.ModelForm):
	class Meta:
		model   = Profile
		fields  = ('rank', 'position', 'sector', 'place', 'phone', 'image',)
		exclude = ['password']
		labels  = {
			'username' : 'ชื่อเข้าใข้งาน',
			'password1': 'รหัสผ่าน',
			'password2': 'ยืนยันรหัสผ้าน',
			'rank'     : 'ยศ',
			'position' : 'ตำแหน่ง',
			'sector'   : 'สังกัด',
			'place'    : 'หน่วย',
			'phone'    : 'หมายเลขโทรศัพท์',
			'image'   : 'รูปประจำตัว',
		}
		widgets = {
			'rank'    : widgets.Select(attrs={'class': 'form-control'}),
			'position': forms.Select(attrs={'class': 'form-control'}),
			'sector': forms.Select(attrs={'class': 'form-control'}),
			'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น สทค.มทบ...'}),
			'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
		}


class RankForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ('name',)
        labels = {
			'name' : 'ชั้นยศ',
		}
        widgets = {
			'name' : forms.TextInput(attrs={'class': 'form-control w3-input', 'placeholder': 'ชื่อเต็ม เช่น พันเอก, จ่าสิบเอก...'}),
		}

  
class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ('name',)
        labels = {
			'name': 'สังกัด',
		}
        widgets = {
			'name' : forms.TextInput(attrs={'class': 'form-control w3-input', 'placeholder': 'สังกัด เช่น ส่วนกลาง, ปก.ทภ...'}),
		}

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('name',)
        labels = {
			'name' : 'ตำแหน่ง',
		}
        widgets = {
			'name' : forms.TextInput(attrs={'class': 'form-control w3-input', 'placeholder': 'ตำแหน่ง'}),
		}

class LineTokenForm(forms.ModelForm):
    class Meta:
        model = LineToken
        fields = ('name', 'token', 'note')
        labels = {
            'name' : 'ชื่อโทเคน',
            'token' : 'Token',
            'note' : 'หมายเหตุ',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'ชื่อโทเคน'}),
            'token' : forms.TextInput(attrs={'class': 'w3-input', 'placeholder': 'Line token...'}),
            'note' : forms.Textarea(attrs={'class': 'w3-input'})
        }