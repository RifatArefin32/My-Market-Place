from django.db import models

# Create your models here.
class Category(models.Mode):
    name = models.CharField(max_length=255)