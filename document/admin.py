from django.contrib import admin

from document.models import Inbox

# Register your models here.

#admin.site.register(Inbox)

@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ('receive_no', 'send_from', 'urgency', 'title', 'receive_date', 'receiver',)
    list_filter = ('receive_no', 'send_from', 'urgency', 'receiver',)
