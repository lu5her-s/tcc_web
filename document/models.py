from django.db import models
from django.contrib.auth.models import Group, User

from account.models import Profile, Sector

# Create your models here.

def get_file_name_inbox(instance, filename):
    rev_no = instance.inbox.receive_no
    return f'DocumentFile/Inbox/{rev_no}/{filename}'

def get_file_name_outbox(instance, filename):
    rev_no = instance.outbox.out_no
    return f'DocumentFile/Outbox/{rev_no}/{filename}'

class Inbox(models.Model):

    """ For Inbox document """
    URGENCY      = [
            ('ปกติ',       'ปกติ'),
            ('ด่วน',       'ด่วน'),
            ('ด่วนมาก',    'ด่วนมาก'),
            ('ด่วนที่สุด',    'ด่วนที่สุด'),
            ]
    TYPE         = [
            ('ปฏิบัติ',      'ปฏิบัติ'),
            ('เพื่อทราบ',   'เพื่อทราบ'),
            ]
    STATUS       = [
            ('รอการปฎิบัติ', 'รอการปฏิบัติ'),
            ('รับ',        'รับ'),
            ('ดำเนินการแล้ว', 'ดำเนินการแล้ว'),
            ]

    receive_no   = models.CharField(max_length=255)
    send_from    = models.CharField(max_length=255)
    doc_no       = models.CharField(max_length=255)
    urgency      = models.CharField(max_length=255, choices=URGENCY, default="ปกติ")
    doc_type     = models.CharField(max_length=255, choices=TYPE, default="เพื่อทราบ")
    title        = models.TextField()
    doc_date     = models.DateField()
    receiver     = models.ForeignKey(User, on_delete=models.CASCADE)
    receive_date = models.DateTimeField(auto_now_add=True)
    set_in       = models.CharField(max_length=255, null=True, blank=True)
    status       = models.CharField(max_length=255, choices=STATUS, default="รับ")
    #doc_file = models.FileField(upload_to=get_file_name)
    assigned_to  = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='assignedUser')
    assigned_group = models.ManyToManyField(Sector, blank=True, related_name='assignedGroup')

    def __str__(self):
        return 'เลขรับที่ ' + self.receive_no + '-' + ' ' + self.doc_no + '- ' + self.title

class InboxFile(models.Model):
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)
    files = models.FileField(upload_to=get_file_name_inbox)

    def __str__(self):
        return 'เลขรับที่ '+ self.inbox.receive_no

class Outbox(models.Model):
    URGENCY      = [
            ('ปกติ',       'ปกติ'),
            ('ด่วน',       'ด่วน'),
            ('ด่วนมาก',    'ด่วนมาก'),
            ('ด่วนที่สุด',    'ด่วนที่สุด'),
            ]
    out_no = models.CharField(max_length=255)
    out_from = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_send')
    send_to = models.ManyToManyField(Sector, blank=True, related_name='receiver')
    send_out = models.CharField(max_length=255, blank=True)
    doc_no = models.CharField(max_length=255)
    urgency = models.CharField(max_length=255, choices=URGENCY, default='ปกติ')
    title = models.CharField(max_length=255)
    doc_date = models.DateTimeField()
    ref_doc = models.ForeignKey(Inbox, on_delete=models.CASCADE, blank=True, null=True, related_name='reference_doc')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")

    def __str__(self):
        return self.out_no + ' ' + self.title

class OutboxFile(models.Model):
    outbox = models.ForeignKey(Outbox, on_delete=models.CASCADE)
    files = models.FileField(upload_to=get_file_name_outbox)

    def __str__(self):
        return self.outbox.out_no
