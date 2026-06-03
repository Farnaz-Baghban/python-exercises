# why we need to make this homepage manually and why it doese not exist by default?
from django.shortcuts import render

def home(request): #can you explain exactly what and how this function/all functions in this project work? like:we start processing the html request coming to our website 
    return render(request, 'home.html')#why in render we again rettrn the request one more time here too?
# next: always after defining your function(how to treat http requests) in views, you need to map it to a url in the app's urls
# q:what was models for? views and models seem really the same both have functions right? views is used to define what happens after each request, usually another page in html is returned(what else?)
# but what happens in model? why is it diffrent from views?