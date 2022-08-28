from django.contrib import admin

from document.models import Inbox, InboxFile, Outbox

# Register your models here.

#admin.site.register(Inbox)

@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('receive_no', 'send_from', 'urgency', 'title', 'receive_date', 'receiver',)
    list_filter = ('receive_no', 'send_from', 'urgency', 'receiver',)

admin.site.register(InboxFile)

@admin.register(Outbox)
class OutboxAdmin(admin.ModelAdmin):
    list_display = ('out_no', 'out_from', 'title', 'doc_date',)
