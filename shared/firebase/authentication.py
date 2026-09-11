from pathlib import Path

import firebase_admin

from firebase_admin import auth
from firebase_admin import credentials

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


BASE_DIR = Path(__file__).resolve().parents[2]

FIREBASE_CREDENTIALS = (
    BASE_DIR / 'firebase-service-account.json'
)


if not firebase_admin._apps:

    cred = credentials.Certificate(
        FIREBASE_CREDENTIALS
    )

    firebase_admin.initialize_app(cred)


class FirebaseAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None

        try:

            scheme, token = auth_header.split()

        except ValueError:

            raise AuthenticationFailed(
                'Formato de autorización inválido.'
            )

        if scheme.lower() != 'bearer':

            raise AuthenticationFailed(
                'Debe utilizar Bearer Token.'
            )

        try:

            decoded_token = auth.verify_id_token(token)

        except Exception:

            raise AuthenticationFailed(
                'Token de Firebase inválido.'
            )

        firebase_uid = decoded_token.get('uid')

        if not firebase_uid:

            raise AuthenticationFailed(
                'El token no contiene un UID.'
            )

        return firebase_uid, decoded_token