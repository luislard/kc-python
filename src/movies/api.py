from rest_framework.generics import ListCreateAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

