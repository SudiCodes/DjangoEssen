from django.db import models


# Create your models here.
class RegularFile(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to="docs/")
    image = models.ImageField(upload_to="imgs/")