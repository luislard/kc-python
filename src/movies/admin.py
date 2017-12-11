from django.contrib import admin

# Register your models here.

from movies.models import Category, Movie


admin.site.register(Category)

# Con esto se personaliza el admin de django
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'release_date', 'rating', 'user_full_name', 'category') # muestra estas columnas en el listado de pelis
    list_filter = ('user', 'category', 'release_date') # agrega los paneles de filtrado a la derecha
    search_fields = ('title', 'director_name', 'summary', 'category__name') # agrega la casilla de buscar y busca por estas columnas

    def user_full_name(self, obj):
        return "{0} {1}".format(obj.user.first_name, obj.user.last_name)
    user_full_name.short_description = "Movie Owner" # en python todo son objetos
    user_full_name.admin_order_field = "user__first_name" # le decimos que ordene por el first name

    readonly_fields = ('created_at', 'modified_at')
    fieldsets = (
        (None, {'fields': ('title', 'summary')}),
        ("Category & Rating", {'fields': ('category', 'rating')}),
        ("Aditional Info", {'fields': ('director_name', 'release_date', 'image', 'user')}),
        ("Creation & modification dates", {'fields': ('created_at', 'modified_at'),
                                           'classes': ('collapse',),
                                           'description': 'This field is autogenerated'}),
    )