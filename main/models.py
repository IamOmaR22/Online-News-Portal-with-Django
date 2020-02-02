from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()  # default="-"
    fb = models.CharField(default="-", max_length=50)
    tw = models.CharField(default="-", max_length=50)
    yt = models.CharField(default="-", max_length=50)
    tell = models.CharField(default="-", max_length=50)
    link = models.CharField(default="-", max_length=50)

    set_name = models.CharField(default="-", max_length=50)

 ## for header and footer logo images start
    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")
 ## for header and footer logo images end

        
    def __str__(self):
        return self.set_name + " | " + str(self.pk)