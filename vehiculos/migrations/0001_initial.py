
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_unico', models.CharField(max_length=50, unique=True)),
                ('patente', models.CharField(max_length=50)),
                ('numero_chasis', models.CharField(max_length=50)),
                ('numero_motor', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('autopartes', models.TextField()),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
            ],
        ),
    ]
