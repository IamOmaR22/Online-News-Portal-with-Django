from __future__ import unicode_literals
from django.db import models

# Create your models here.

class BlackList(models.Model):
    ip = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.ip