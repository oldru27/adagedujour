from django.db import models

# Create your models here.


class blog2(models.Model):
    titre = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', default='SOME STRING')
    texte = models.TextField(default='SOME STRING')
