from __future__ import unicode_literals
from django.db import models

# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=200)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12,default="00:00")
    picname = models.TextField()
    picurl = models.TextField(default="-")
    writer = models.CharField(max_length=100)
    catname = models.CharField(max_length=100, default="-")   # default="-" for charfield
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)  # ocatid means original cat id.for count news
    show = models.IntegerField(default=0)   # default=0 for integer field-when i use this in existing models
    tag = models.TextField(default="")   # For tag (Filtering)
    act = models.IntegerField(default=0)  # For Publish News
    rand = models.IntegerField(default=0)  # For Random Numbers

        
    def __str__(self):
        return self.name