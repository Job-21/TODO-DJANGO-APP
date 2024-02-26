from django.db import models

# Create your models here.
class ToDoData(models.Model):
    task = models.CharField(max_length=1000)
    def __str__(self):
        return self.task