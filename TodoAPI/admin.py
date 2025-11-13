from django.contrib import admin  
from .models import Todoitem
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = (
    "title",
    "body",
    "completed",
    "created_at",
    "updated_at",
    )
admin.site.register(Todoitem, TodoAdmin)
