from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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

    def __str__(self):
        return self.name
        
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    comment_textfield = models.TextField()