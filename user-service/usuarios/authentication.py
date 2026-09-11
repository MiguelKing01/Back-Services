from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from .models import Usuario


class UsuarioJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):

        user_id = validated_token.get('id_user')

        if user_id is None:
            raise AuthenticationFailed(
                'El token no contiene id_user',
                code='token_not_valid'
            )

        try:
            usuario = Usuario.objects.get(id_user=user_id)
        except Usuario.DoesNotExist:
            raise AuthenticationFailed(
                'Usuario no encontrado',
                code='token_not_valid'
            )

        if usuario.activo != 1:
            raise AuthenticationFailed(
                'El usuario está inactivo',
                code='token_not_valid'
            )

        return usuario