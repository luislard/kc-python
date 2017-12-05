from django.contrib import admin

# Register your models here.

from movies.models import Category, Movie

admin.site.register(Category)

admin.site.register(Movie)