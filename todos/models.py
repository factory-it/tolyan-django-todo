from django.db import models

# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.title