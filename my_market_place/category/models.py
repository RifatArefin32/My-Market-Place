from django.db import models

class Category(models.Model): 
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name