#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : models.py
# Author            : lu5her <lu5her@mail>
# Date              : Sun Sep, 04 2022, 23:52 247
# Last Modified Date: Sun Sep, 04 2022, 23:52 247
# Last Modified By  : lu5her <lu5her@mail>

from django.db import models
from django.contrib.auth.models import Group, User

from account.models import Profile, Sector

# Create your models here.

# def get_file_name_inbox(instance, filename):
    # rev_no = instance.inbox.receive_no
    # return f'DocumentFile/Inbox/{rev_no}/{filename}'

# def get_file_name_outbox(instance, filename):
    # rev_no = instance.outbox.out_no
    # return f'DocumentFile/Outbox/{rev_no}/{filename}'
def get_file_name(instance, filename):
    return f'Document/%Y/%m/%d/{filename}'

class Document(models.Model):

    """ For Inbox document """
    URGENCY      = [
            ('ปกติ',       'ปกติ'),
            ('ด่วน',       'ด่วน'),
            ('ด่วนมาก',    'ด่วนมาก'),
            ('ด่วนที่สุด',    'ด่วนที่สุด'),
            ]
    # TYPE         = [
            # ('ปฏิบัติ',      'ปฏิบัติ'),
            # ('เพื่อทราบ',   'เพื่อทราบ'),
            # ]
    # STATUS       = [
            # ('รอการปฎิบัติ', 'รอการปฏิบัติ'),
            # ('รับ',        'รับ'),
            # ('ดำเนินการแล้ว', 'ดำเนินการแล้ว'),
            # ]

    #receive_no   = models.CharField(max_length=255)
    #send_from    = models.CharField(max_length=255)
    document_no    = models.CharField(max_length=255)
    urgency        = models.CharField(max_length=255, choices=URGENCY, default="ปกติ")
    #doc_type     = models.CharField(max_length=255, choices=TYPE, default="เพื่อทราบ")
    title          = models.TextField()
    document_date  = models.DateField()
    #receiver     = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at     = models.DateTimeField(auto_now_add=True)
    set_in         = models.CharField(max_length=255, null=True, blank=True)
    #status       = models.CharField(max_length=255, choices=STATUS, default="รับ")
    #doc_file = models.FileField(upload_to=get_file_name)
    assigned_to    = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='assignedUser')
    assigned_group = models.ManyToManyField(Sector, blank=True, related_name='assignedGroup')
    document_file  = models.FileField(upload_to=get_file_name)
    author         = models.ForeignKey(User, on_delete=models.CASCADE)
    document_ref   = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'เลขรับที่ ' + self.receive_no + '-' + ' ' + self.document_no + '- ' + self.title

class Download(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    couter   = models.PositiveSmallIntegerField(default=0)

class Accept(models.Model):
    document    = models.ForeignKey(Document, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{document.document_no} Accept by {user.get_full_name}'
