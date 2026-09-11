from django.db import models


class Envio(models.Model):

    id_envio = models.AutoField(
        primary_key=True
    )

    codigo_entrega = models.CharField(
        max_length=50,
        unique=True
    )

    id_estudiante = models.IntegerField()

    id_tarea = models.IntegerField()

    titulo_trabajo = models.CharField(
        max_length=200
    )

    descripcion = models.TextField(
        null=True,
        blank=True
    )

    archivo_url = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=50,
        default='entregado'
    )

    calificacion = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    activo = models.IntegerField(
        default=1
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    fecha_limite = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'envios'

    def __str__(self):
        return f"Entrega {self.codigo_entrega} - {self.titulo_trabajo}"

