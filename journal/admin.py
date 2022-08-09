from django.contrib import admin

from journal.models import Journal, JournalType, JournalStatus, JournalImage

# Register your models here.

# admin.site.register(Journal)
admin.site.register(JournalType)
admin.site.register(JournalStatus)
admin.site.register(JournalImage)

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'author', 'status', 'created_at',)
    list_filter = ('category', 'title', 'author', 'status')