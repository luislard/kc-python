from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class HelloWorld(APIView):

    def get(self, request):
        return Response([ 'hello','world' ])

    def post(self, request):
        return Response(request.data)

    def put(self, request):
        return Response(request.data)


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()
        # tenemos que devolver en el response datos primitivos integers, floats, booleans, tuples, lists, dictionaries, strings
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)