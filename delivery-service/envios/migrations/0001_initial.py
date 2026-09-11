from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id_envio', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_entrega', models.CharField(max_length=50, unique=True)),
                ('id_estudiante', models.IntegerField()),
                ('id_tarea', models.IntegerField()),
                ('titulo_trabajo', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('archivo_url', models.CharField(blank=True, max_length=500, null=True)),
                ('estado', models.CharField(default='entregado', max_length=50)),
                ('calificacion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('activo', models.IntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_limite', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'envios',
            },
        ),
    ]

