from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
  
        return f"{self.title} - Created: {self.created.strftime('%Y-%m-%d %H:%M:%S')}, Completed: {self.completed_at.strftime('%Y-%m-%d %H:%M:%S')}"
      
