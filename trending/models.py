from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Trending(models.Model):
    txt = models.CharField(max_length=200)
    
    def __str__(self):
        return self.txt