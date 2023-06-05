from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

class Index(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    subtitle = models.TextField()
