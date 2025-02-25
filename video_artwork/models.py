from django.db import models

# Create your models here.
class Videoedits(models.Model):
    name=models.CharField(max_length=32)
    url=models.CharField(max_length=100)
    date=models.DateField()
    description=models.CharField(max_length=100)