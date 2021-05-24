from django.contrib import admin
from .models import task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'notes',
        'complete',
        'person',
    )


admin.site.register(task, TaskAdmin)
