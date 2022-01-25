from django.shortcuts import render
from .models import VideoUplod

# Create your views here.
def index(request):
    all_video = VideoUplod.objects.all()
    return render(request, 'home.html',{"all_video":all_video})
