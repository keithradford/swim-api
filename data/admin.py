from django.contrib import admin
from .models import Swimmer, Coach, Club

class SwimmerAdmin(admin.ModelAdmin):
    readonly_fields = ('age',)

admin.site.register(Swimmer, SwimmerAdmin)
admin.site.register(Coach)
admin.site.register(Club)
