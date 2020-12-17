from django.db import models

# Create your models here.

class Sample(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    sound = models.FileField(upload_to='sounds/wav/')
    
    def __str__(self):
        return self.title
