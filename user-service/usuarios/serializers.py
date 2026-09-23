# pyrefly: ignore [missing-import]
from rest_framework import serializers
# pyrefly: ignore [missing-import]
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'contrasena_user': {
                'write_only': True
            }
        }


