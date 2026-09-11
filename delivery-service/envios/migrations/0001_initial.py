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
                ('numero_guia', models.CharField(max_length=50, unique=True)),
                ('id_usuario', models.IntegerField()),
                ('id_empresa', models.IntegerField(blank=True, null=True)),
                ('direccion_origen', models.CharField(max_length=255)),
                ('direccion_destino', models.CharField(max_length=255)),
                ('destinatario_nombre', models.CharField(max_length=100)),
                ('destinatario_telefono', models.CharField(max_length=20)),
                ('estado', models.CharField(default='pendiente', max_length=50)),
                ('costo_envio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('activo', models.IntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega_estimada', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'envios',
            },
        ),
    ]
