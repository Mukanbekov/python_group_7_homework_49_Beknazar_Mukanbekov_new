from django.contrib import admin

# Register your models here.
from webapp.models import List, Status, Type, Project


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['id', 'name', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(List, ListAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
