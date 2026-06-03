from django.urls import path
# linking views to urls
# from current directory import module views
from . import views
app_name = 'movies'

urlpatterns = [
    # define url endpoints
    # here we use relative urls
    
    path('', views.index, name='index')  ,#what is the diffrence between what goese here and how it goese here with what goese in main urls.py?
    path('<int:movie_id>/',views.detail, name='detail'),
    
    # means root, the path a refrence to the function in views
    # (do not call it with (), just pass a refrence to it)
    # the name the url
]
# now our main app! needs to be informed of the movies app!


