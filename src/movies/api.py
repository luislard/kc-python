from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from movies.models import Movie
from movies.permissions import MoviesPermission
from movies.serializers import MovieSerializer, MoviesListSerializer


class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly] # esta clase hace que la lista este abierta pero la creacion no

    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer

    # documentacion en http://www.django-rest-framework.org/api-guide/generic-views/
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [MoviesPermission]

    # documentacion en http://www.django-rest-framework.org/api-guide/generic-views/
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
