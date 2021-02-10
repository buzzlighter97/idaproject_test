from django.contrib import admin
from . import models

class ImageAdmin(admin.ModelAdmin):

    list_display = ("name", "width", "height") 

    search_fields = ("name",) 

admin.site.register(models.ImageModel, ImageAdmin)
