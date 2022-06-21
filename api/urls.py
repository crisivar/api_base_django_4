from django.http import JsonResponse
from django.urls import path
from django.conf.urls import include

from rest_framework import status


def test():
    return lambda req: JsonResponse({"result": "ok"}, status=status.HTTP_200_OK)


urlpatterns = [
    path('test/', test() , name = 'test'),
    path("users/", include("users.urls")),
]
