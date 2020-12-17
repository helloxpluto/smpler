from django.db import models

# Create your models here.

class Sample(models.Model):
    title = models.CharField(max_length=50)
    sound = models.FileField(upload_to=None)
    
    def __str__(self):
        return self.title
