from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, null=False)
    age = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
