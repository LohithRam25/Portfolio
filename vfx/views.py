from django.shortcuts import render
from .models import Videos
# Create your views here.
def vfx_post(request):
    videos=Videos.objects.all()
    return render(request,"vfx_post.html",{"videos":videos})