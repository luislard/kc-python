from django.http import HttpResponse


from movies.models import Movie

# definimos una funcion
def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello World!")
    else:
        return HttpResponse("Hello " + name)


def home(request):
    movies = Movie.objects.all()
    html = "<ul>"
    for movie in movies:
        html += "<li>" + movie.title + "</li>"
    html += "</ul>"
    return HttpResponse(html)
