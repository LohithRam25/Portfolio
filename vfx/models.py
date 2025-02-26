from django.db import models

class Videos(models.Model):
    name=models.CharField(max_length=31)
    video_url=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date=models.DateField()
    posted_date=models.DateField()