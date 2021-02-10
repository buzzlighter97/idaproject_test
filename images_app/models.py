from django.db import models
from django.db.models.fields.files import ImageField

class ImageModel(models.Model):
    height = models.PositiveIntegerField(verbose_name='Высота')
    width = models.PositiveIntegerField(verbose_name='Ширина')
    name = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='images/')