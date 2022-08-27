from django.db import models
from django.contrib.auth.models import Group, User

from account.models import Profile, Sector

# Create your models here.

def get_file_name(instance):
    rev_no = instance.inbox.receive_no
    return f'DocumentFile/{rev_no}'

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
    assigned_group = models.ManyToManyField(Sector, null=True, blank=True, related_name='assignedGroup')

    def __str__(self):
        if self.receiver.first_name:
            return self.receive_no + '-' + str(self.receive_date) + ' ' + self.receiver.get_full_name()
        else:
            return self.receive_no, self.receive_date, self.receiver

class InboxFile(models.Model):
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_file_name)

    def __str__(self):
        return self.inbox.receive_no

class Outbox(models.Model):

    """For Outbox sending doument"""
    pass
