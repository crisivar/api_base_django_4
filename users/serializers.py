from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from rest_framework import serializers

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "nivel_acceso",
            "tpo_prsna",
            "first_name",
            "last_name",
            "nm_emprsa",
            "cc_nit",
            "email",
            "tlfno",
            "ciudad",
            "pais",
            "role",
            "token_password",
            "password_updated",
            "date_password_updated",
            "last_login",
            "is_superuser",
            "is_staff"
            ]
