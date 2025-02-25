from django.db import models

class Videos(models.Model):
    name=models.CharField(max_length=31)
    video=models.FileField(upload_to="vfx_post")
    date=models.DateField()