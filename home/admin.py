from django.contrib import admin

from .models import Settings 
# Register your models here.
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    readonly_fields = ('image_tag',)
admin.site.register(Settings,SettingsAdmin)
