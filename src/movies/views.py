from django.http import HttpResponse

# definimos una funcion
def hello_world(request):
    return HttpResponse("Hello World!")
