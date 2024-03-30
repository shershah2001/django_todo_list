from django.contrib import admin
from todolist.models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('id','task_title','task_description','due_date','due_time','completed')
