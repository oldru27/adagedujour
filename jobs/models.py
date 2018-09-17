from django.db import models
from datetime import datetime

# Create your models here.
class job(models.Model):
    titre = models.CharField(max_length=150, default='')
    imagefun= models.ImageField(upload_to='images/')
    summary = models.TextField(default='Une description courte')
    fullsummary = models.TextField(default='Un récit')
    date = models.DateTimeField(default=datetime.now, blank=True)
