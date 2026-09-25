# pyrefly: ignore [missing-import]
from rest_framework import serializers
<<<<<<< HEAD
=======
# pyrefly: ignore [missing-import]
from rest_framework_simplejwt.tokens import RefreshToken
>>>>>>> f72d74c67228fa038055226b6b185960280e30f2
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'
        extra_kwargs = {
            'contrasena_user': {
                'write_only': True
            }
        }


>>>>>>> f72d74c67228fa038055226b6b185960280e30f2
