from django.shortcuts import render
from .models import Videoedits
# Create your views here.
def videos(request):
    videos1=Videoedits.objects.all()
    print(videos1)

    return render(request,"video_edits.html",{"videos1":videos1})