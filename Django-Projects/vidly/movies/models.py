from django.db import models
from django.utils import timezone
# Create your models here.
# add a class called genre
# direct this class , inherit from models.Model -> encapsulates functionalities around DATABASE
# define class attributes rows and fields
# define name, 
# defime a movie class
# inherit
# give it title, year, number in stock
# daily rate ->float 
# genre ->foreignkey -> build relationship with other classes
# explain: ForeignKey
# create an on_delete configuration ->cascade
class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    Genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    
    date_created = models.DateTimeField(default=timezone.now)#do not call it just pass it or date will be hardcoded
    
# NEXT STEP: store model in a database
# PREV STEP: define the app in main urls
# PREV PREV STEP: linking app's views in app's urls