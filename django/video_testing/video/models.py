from django.db import models

# Create your models here.
class VideoUplod(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    video = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title