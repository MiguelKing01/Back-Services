# pyrefly: ignore [missing-import]
from rest_framework import viewsets
# pyrefly: ignore [missing-import]
from rest_framework.views import APIView
# pyrefly: ignore [missing-import]
from rest_framework.permissions import AllowAny, IsAuthenticated
# pyrefly: ignore [missing-import]
from rest_framework.response import Response
from config.authentication import FirebaseAuthentication

from .models import Usuario
from .serializers import UsuarioSerializer, LoginSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'firebase_uid') and user.firebase_uid:
            if self.request.query_params.get('todos') == 'true':
                return Usuario.objects.all()
            return Usuario.objects.filter(firebase_uid=user.firebase_uid)
        return super().get_queryset()

    def perform_create(self, serializer):
        user = self.request.user
        firebase_uid = getattr(user, 'firebase_uid', None)
        if firebase_uid:
            serializer.save(firebase_uid=firebase_uid)
        else:
            serializer.save()
