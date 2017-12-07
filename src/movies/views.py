from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from movies.forms import MovieForm
from movies.models import Movie

# definimos una funcion
def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello World!")
    else:
        return HttpResponse("Hello " + name)


def home(request):
    latest_movies = Movie.objects.all().order_by('-release_date')
    context = { 'movies': latest_movies[:3] }
    return render(request, "home.html", context)


def movie_detail(request, pk):
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")
    if len(possible_movies) == 0:
        # pelicula no existe
        return render(request,"404.html", status=404)
    else:
        # pelicula existe
        movie = possible_movies[0]
        context = { 'movie': movie }
        return render(request, "movie_detail.html", context)


class CreateMovieView(View):

    def get(self, request):
        form = MovieForm()
        return render(request,'movie_form.html', {'form': form})