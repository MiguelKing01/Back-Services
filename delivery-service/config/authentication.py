import os
import firebase_admin
from firebase_admin import auth, credentials
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


def get_firebase_app():
    if not firebase_admin._apps:
        cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH', 'firebase-credentials.json')
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            return firebase_admin.initialize_app(cred)
        else:
            try:
                return firebase_admin.initialize_app()
            except Exception:
                pass
    return firebase_admin.get_app()


class FirebaseUser:
    """Clase wrapper para representar al usuario autenticado por Firebase en DRF"""
    def __init__(self, uid, email=None, claims=None):
        self.uid = uid
        self.firebase_uid = uid
        self.email = email
        self.claims = claims or {}
        self.is_authenticated = True

    @property
    def is_anonymous(self):
        return False

    def __str__(self):
        return f"FirebaseUser({self.uid})"


class FirebaseAuthentication(BaseAuthentication):
    """
    Autenticador personalizado para Django REST Framework con Firebase Auth.
    Espera la cabecera: Authorization: Bearer <FIREBASE_ID_TOKEN>
    """
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return None

        id_token = parts[1]

        get_firebase_app()

        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception as e:
            raise AuthenticationFailed(f'Token de Firebase inválido o expirado: {str(e)}')

        uid = decoded_token.get('uid')
        email = decoded_token.get('email')

        user = FirebaseUser(uid=uid, email=email, claims=decoded_token)
        return (user, decoded_token)

    def authenticate_header(self, request):
        return 'Bearer realm="api"'
