from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    Tag_Choice = (
              ('Games', 'Games'),
              ('Anime', 'Anime'),
              ('Vlog', 'Vlog'),
          )
          
    name = models.CharField(max_length=200)
    video_img = models.FileField()
    tag = models.CharField(max_length=20,choices=Tag_Choice,default='Games')
    video_file = models.FileField()