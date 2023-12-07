from django.db import models

# Create your models here.
class massage(models.Model):
    image = models.ImageField(upload_to='img')
    heading = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.heading

class blog(models.Model):
    picture = models.ImageField(upload_to='img2')
    topnote = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.topnote