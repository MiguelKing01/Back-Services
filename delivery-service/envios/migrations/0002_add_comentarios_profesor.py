from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='comentarios_profesor',
            field=models.TextField(blank=True, null=True),
        ),
    ]
