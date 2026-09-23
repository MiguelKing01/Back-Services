from firebase_admin import auth as firebase_auth
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from . import firebase_init  # fuerza la inicialización del SDK
from .models import Company


class FirebaseAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            prefix, token = auth_header.split(' ')
        except ValueError:
            raise AuthenticationFailed('Formato inválido. Usa: Bearer <token>')

        if prefix != self.keyword:
            raise AuthenticationFailed(f'Prefijo inválido, se esperaba "{self.keyword}"')

        try:
            decoded_token = firebase_auth.verify_id_token(token)
        except firebase_auth.ExpiredIdTokenError:
            raise AuthenticationFailed('El token ha expirado')
        except firebase_auth.InvalidIdTokenError:
            raise AuthenticationFailed('Token inválido')
        except Exception:
            raise AuthenticationFailed('No se pudo verificar el token')

        firebase_uid = decoded_token.get('uid')

        try:
            company = Company.objects.get(firebase_uid=firebase_uid, activo=1)
        except Company.DoesNotExist:
            raise AuthenticationFailed('No existe una empresa asociada a esta cuenta de Firebase')

        return (company, decoded_token)