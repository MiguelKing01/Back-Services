from rest_framework import serializers
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


class LoginSerializer(serializers.Serializer):

    correo_user = serializers.EmailField()
    contrasena_user = serializers.CharField(write_only=True)

    def validate(self, attrs):

        try:
            usuario = Usuario.objects.get(
                correo_user=attrs['correo_user']
            )
        except Usuario.DoesNotExist:
            raise serializers.ValidationError(
                "Correo o contraseña incorrectos."
            )

        # Actualmente las contraseñas están en texto plano
        if attrs['contrasena_user'] != usuario.contrasena_user:
            raise serializers.ValidationError(
                "Correo o contraseña incorrectos."
            )

        if usuario.activo != 1:
            raise serializers.ValidationError(
                "El usuario está inactivo."
            )

        refresh = RefreshToken()

        refresh['id_user'] = usuario.id_user
        refresh['correo_user'] = usuario.correo_user
        refresh['tipo_user'] = usuario.tipo_user

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }