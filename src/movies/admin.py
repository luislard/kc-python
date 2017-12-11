from django.contrib import admin

# Register your models here.

from movies.models import Category, Movie


admin.site.register(Category)

# Con esto se personaliza el admin de django
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'release_date', 'rating', 'user', 'category')
    list_filter = ('user', 'category', 'release_date')
    search_fields = ('title', 'director_name', 'summary')

