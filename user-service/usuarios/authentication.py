from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from shared.firebase.authentication import FirebaseAuthentication

from .models import Usuario


class UsuarioFirebaseAuthentication(BaseAuthentication):

    def authenticate(self, request):

        resultado = FirebaseAuthentication().authenticate(request)

        if resultado is None:
            return None

        firebase_uid, decoded_token = resultado

        try:

            usuario = Usuario.objects.get(
                firebase_uid=firebase_uid
            )

        except Usuario.DoesNotExist:

            raise AuthenticationFailed(
                'El usuario no está registrado en el sistema.'
            )

        if usuario.activo != 1:

            raise AuthenticationFailed(
                'El usuario está inactivo.'
            )

        return usuario, decoded_token