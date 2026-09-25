from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from config.authentication import FirebaseAuthentication
from .models import Envio
from .serializers import EnvioSerializer


class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Envio.objects.all()
        id_estudiante = self.request.query_params.get('id_estudiante')
        id_tarea = self.request.query_params.get('id_tarea')
        codigo_entrega = self.request.query_params.get('codigo_entrega')
        estado = self.request.query_params.get('estado')
        activo = self.request.query_params.get('activo')

        if id_estudiante is not None:
            queryset = queryset.filter(id_estudiante=id_estudiante)
        if id_tarea is not None:
            queryset = queryset.filter(id_tarea=id_tarea)
        if codigo_entrega is not None:
            queryset = queryset.filter(codigo_entrega=codigo_entrega)
        if estado is not None:
            queryset = queryset.filter(estado=estado)
        if activo is not None:
            queryset = queryset.filter(activo=activo)

        return queryset

