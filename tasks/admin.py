from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Displayed fields in the list view of the Task model.
    list_display = ('title', 'description', 'due_date', 'status', 'owner')

    # Fields used for searching in the Django admin interface.
    search_fields = ('title', 'owner__username')
