from django.shortcuts import render
from .models import Blenderpost
# Create your views here.
def posts(request):
    posts=Blenderpost.objects.all()
    return render(request,"blender_post.html",{"posts":posts})