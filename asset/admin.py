from django.contrib import admin

from asset.models import (
    Asset,
    AssetModel,
    AssetStatus,
    AssetType,
    Location,
    Manufacturer,
    Network,
    Supplier,
)

# Register your models here.

@admin.register(Asset)
class AdminAsset(admin.ModelAdmin):
    list_display = ('name', 'model_no', 'serial_no', 'assigned_to', 'status', 'supplier', 'request_able', 'location_at', 'manufacturer', 'quantity', 'on_network', 'asset_type',)
    list_filter =('name', 'model_no', 'serial_no', 'assigned_to', 'status', 'supplier', 'request_able', 'location_at', 'manufacturer', 'quantity', 'on_network', 'asset_type',)
    search_fields = ('name', 'model_no', 'serial_no', 'assigned_to', 'status', 'supplier', 'location_at', 'manufacturer', 'quantity', 'on_network', 'asset_type',)

admin.site.register(AssetModel)
admin.site.register(AssetStatus)
admin.site.register(AssetType)
admin.site.register(Location)
admin.site.register(Manufacturer)
admin.site.register(Network)
admin.site.register(Supplier)
