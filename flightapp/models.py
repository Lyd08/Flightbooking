from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField()
    user = models.CharField(max_length=100)