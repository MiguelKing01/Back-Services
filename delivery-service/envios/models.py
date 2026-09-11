from django.db import models


class Envio(models.Model):

    id_envio = models.AutoField(
        primary_key=True
    )

    numero_guia = models.CharField(
        max_length=50,
        unique=True
    )

    id_usuario = models.IntegerField()

    id_empresa = models.IntegerField(
        null=True,
        blank=True
    )

    direccion_origen = models.CharField(
        max_length=255
    )

    direccion_destino = models.CharField(
        max_length=255
    )

    destinatario_nombre = models.CharField(
        max_length=100
    )

    destinatario_telefono = models.CharField(
        max_length=20
    )

    estado = models.CharField(
        max_length=50,
        default='pendiente'
    )

    costo_envio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    activo = models.IntegerField(
        default=1
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_entrega_estimada = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'envios'

    def __str__(self):
        return f"Envio {self.numero_guia} - {self.destinatario_nombre}"
