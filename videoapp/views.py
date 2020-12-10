from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def v_main(request):
    videos = Video.objects.all()
    context = {'videos':videos}
    return render(request, "videoapp/main.html", context)