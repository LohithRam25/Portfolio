from django.db import models

# Create your models here.
class Blenderpost(models.Model):
    name=models.CharField(max_length=32)
    image=models.ImageField(upload_to='blender_posts')
    date=models.DateField()
    posted_date=models.DateField()
    details=models.CharField(max_length=500)
