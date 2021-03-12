from django.contrib import admin

# Register your models here.
from webapp.models import List, Status, Type


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'type', 'created_at', 'updated_at']
    list_filter = ['name']
    search_fields = ['name', 'status', 'type']
    fields = ['id', 'name', 'description', 'status', 'type']
    readonly_fields = ['id']


admin.site.register(List, ListAdmin)
admin.site.register(Status)
admin.site.register(Type)
