from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    content = models.CharField()
    img_url = models.CharField()
    category = models.CharField()

class Category(models.Model):
    name = models.CharField()