from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} ({self.description})"