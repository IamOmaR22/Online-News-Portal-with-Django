from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Comment(models.Model):

    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    cm = models.TextField()
    news_id = models.IntegerField()
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    status = models.IntegerField(default=0) # to give permission a comment

    def __str__(self):
        return self.name
