from django.contrib import admin

# Register your models here.
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') #put these in a tuple()
    
class MovieAdmin(admin.ModelAdmin):
    exclude = ('year',)
    list_display = ('id', 'title', 'Genre', 'number_in_stock', 'daily_rate')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)