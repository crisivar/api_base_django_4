from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import MyTokenObtainPairSerializer

from rest_framework import status
from rest_framework.response import Response
from users.models import User
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from users.serializers import ProfileSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        try:

            profile = User.objects.get(pk=request.user.id)
            if profile:
                serializer = ProfileSerializer(profile, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response([], status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
