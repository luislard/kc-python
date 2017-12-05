from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie

# definimos una funcion
def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello World!")
    else:
        return HttpResponse("Hello " + name)


def home(request):
    movies = Movie.objects.all().order_by('-release_date')
    html = "<ul>"
    context = { 'movies': movies }
    return render(request, "home.html", context)
