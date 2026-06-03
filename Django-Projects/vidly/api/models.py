from django.db import models
from tastypie.resources import ModelResource #tastipy looks for an inner class in our class called Meta
from movies.models import Movie

# Create your models here.
# restfull apis=representional state transfer->how apps shall talk oer http
# models = resources
# movie here is a resource
# uniform resource locater = url

class MovieResource(ModelResource):
    class Meta:
        # class QuerySet(models.QuerySet):
        #     pass
        queryset = Movie.objects.all()#this is a form of lazy loading because all() is just a query object, it only returns a query
        resource_name = 'movies' #next step is to generate our url endpoints
        # -------------------------
        # data we dont wanna expose->
        excludes = ['year']
        
    # all our movies objects will be serialized as json --- which part of this code defines that?