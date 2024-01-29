from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS_CHOICES = [
    ["PENDING", "PENDING"],
    ["INPROGRESS", "INPROGRESS"],
    ["COMPLETED", "COMPLETED"],
]

class Task(models.Model):
    """
    Model representing a task with title, description, due date, status, and owner.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def is_overdue(self):
        return self.due_date < timezone.now().date()
    
    class Meta:
        ordering = ("-id",)
