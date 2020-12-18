from django.db import models

# Create your models here.

class Sample(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    sound = models.FileField(upload_to='media', blank=True)
    url = models.URLField(max_length=200, blank=True)
    
    
    def __str__(self):
        return self.title
