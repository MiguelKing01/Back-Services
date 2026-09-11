from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario

        fields = [
            'id_user',
            'firebase_uid',
            'tipo_user',
            'documento_user',
            'nombres_user',
            'apellidos_user',
            'correo_user',
            'telefono_user',
            'programa',
            'semestre',
            'activo',
            'fecha_creacion',
        ]

        read_only_fields = [
            'id_user',
            'firebase_uid',
            'fecha_creacion',
        ]