from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_image_name(instance, filename):
    image_name = instance.name
    return "assets/{}/{}".format(image_name, filename)

class AssetModel(models.Model):
    ''' Model no '''
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class AssetStatus(models.Model):
    ''' สถานะของทรัพย์สิน เช่น พร้อมใช้งาน กำลังใช้งาน'''
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    """ บริษัทคู่ค้า """
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.name 

class Location(models.Model):
    """ สถานที่ติดตั้ง หรือ ที่อยู่ปัจจุบัน เช่น คลัง หรือ มทบ """
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    l_tel = models.CharField(max_length=10, null=True, blank=True)
    a_tel = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.name + ' ' + str(self.city)

class Manufacturer(models.Model):
    """ บริษัทที่ผลิต """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Network(models.Model):
    """ network """
    name = models.CharField(max_length=200)
    ip_addr = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name + " @ " + self.ip_addr
    
class AssetType(models.Model):
    """ ประเภทของทรัพย์สิน """
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Asset(models.Model):
    name = models.CharField(max_length=200)
    model_no = models.ForeignKey(AssetModel, null=True, blank=True, on_delete=models.CASCADE, related_name='assets_model')
    serial_no = models.CharField(max_length=200)
    purchase_date = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned', null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=get_image_name, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(AssetStatus, on_delete=models.CASCADE)
    warranty_month = models.CharField(max_length=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    request_able = models.BooleanField(default=False)
    location_at = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    on_network = models.ForeignKey(Network, on_delete=models.CASCADE, null=True, blank=True)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name + ' ' + self.serial_no + ' ' + '(' + self.quantity + ')'