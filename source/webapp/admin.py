from django.contrib import admin

# Register your models here.
from webapp.models import List, Status, Type


admin.site.register(List)
admin.site.register(Status)
admin.site.register(Type)
