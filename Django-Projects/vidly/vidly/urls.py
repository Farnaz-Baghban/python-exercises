"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from movies import urls,views
from api.models import MovieResource #we need to import our model
# next we need to create an instance of this class, why?why here?why not in models?
movie_resource = MovieResource()#why do we need to assign these tnto variables here?
# movie_resource.urls #what this means ?
# why api has no urls.py and we call it in the main urls.py? 

# urls is like a map

from . import views

urlpatterns = [
    path('', views.home ), # we need to create a template, if we add it to the main folder we have to add it as an app while it is not an app
    # you need to register this as an app in settings.py, in the list of installed app u add a configuration class 
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls)),#why we did not do it for movies.urls?
    
]
