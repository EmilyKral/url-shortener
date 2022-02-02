from enum import unique
from django.db import models

# Create your models here.
class URL(models.Model):
    original_url = models.TextField(max_length=256)
    # short_url = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return str(self.id)