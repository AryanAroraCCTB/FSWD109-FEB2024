from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.description} on {self.created_at}"

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
