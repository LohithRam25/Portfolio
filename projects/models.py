from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=32)
    github=models.CharField(max_length=100)
    languages=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    started_date=models.DateField()
    conclusion_date=models.DateField()
