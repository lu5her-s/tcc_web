from django.contrib import admin

from document.models import Document

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_no', 'urgency', 'title',)
    list_filter = ('document_no', 'title',)
