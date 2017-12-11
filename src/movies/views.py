from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from movies.forms import MovieForm
from movies.models import Movie
from django.contrib import messages

# definimos una funcion
def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello World!")
    else:
        return HttpResponse("Hello " + name)


@login_required
def home(request):
    latest_movies = Movie.objects.all().order_by('-release_date')
    context = { 'movies': latest_movies[:10] }
    return render(request, "home.html", context)


@login_required
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


class CreateMovieView(LoginRequiredMixin, View):

    def get(self, request):
        form = MovieForm()
        return render(request,'movie_form.html', {'form': form})

    def post(self, request):
        movie = Movie()
        movie.user = request.user # asignamos a la pelicula el usuario autenticado
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            form = MovieForm()
            url = reverse('movie_detail_page', args=[movie.pk])
            message = "Movie created succesfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request,message)
        return render(request,'movie_form.html', {'form': form})


class MyMoviesView(ListView):
    model = Movie
    template_name = "my_movies.html"

    def get_queryset(self):
        queryset = super(MyMoviesView, self).get_queryset()
        return queryset.filter(user=self.request.user)
