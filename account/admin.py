from django.contrib import admin
from account.models import Profile, Sector, Rank, Position, LineToken

# Register your models here.

admin.site.register(Profile)
admin.site.register(Sector)
admin.site.register(Rank)
admin.site.register(Position)
admin.site.register(LineToken)