from django.db import models


class Usuario(models.Model):

    id_user = models.AutoField(
        primary_key=True
    )

    tipo_user = models.CharField(
        max_length=20
    )

    documento_user = models.CharField(
        max_length=20,
        unique=True
    )

    nombres_user = models.CharField(
        max_length=100
    )

    apellidos_user = models.CharField(
        max_length=100
    )

    correo_user = models.EmailField(
        unique=True
    )

    contrasena_user = models.CharField(
        max_length=128
    )

    telefono_user = models.CharField(
        max_length=20,
        blank=True
    )

    programa = models.CharField(
        max_length=150
    )

    semestre = models.IntegerField(
        null=True,
        blank=True
    )

    activo = models.IntegerField(
        default=1
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nombres_user} {self.apellidos_user}"