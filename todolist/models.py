from django.db import models

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField(null=True,blank=True)
    due_date  = models.DateField()
    due_time = models.TimeField()
    completed= models.BooleanField(default=False)
