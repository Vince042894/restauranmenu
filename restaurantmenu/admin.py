from django.contrib import admin
from .models import Item

admin.site.site_header = "Yummy Philippines Administration"
admin.site.site_title = "Yummy Philippines Admin Portal"
admin.site.index_title = "Welcome to the Yummy Philippines Admin Panel"

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status", )
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)
