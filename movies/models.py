from django.db import models
from django.contrib.auth.models import User
import datetime



class Category(models.Model):
    catname = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return self.catname

class Movie(models.Model):
    MName = models.CharField(max_length=600)
    discription = models.CharField(max_length=1200)
    year = models.IntegerField()
    Category = models.ForeignKey(Category , on_delete= models.CASCADE)
    uploader = models.ForeignKey(User , on_delete= models.CASCADE)
    img = models.ImageField(upload_to='movies/')
    trailer = models.URLField()
    rating = models.IntegerField()

    def __str__(self):
        return self.MName