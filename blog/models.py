from django.db import models

# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=500)
    blog = models.TextField()
    image = models.ImageField(upload_to = "blog/images", default = None, blank = True, null = True)