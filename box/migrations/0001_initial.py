# Generated by Django 4.1.6 on 2023-03-08 05:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('dimension_height', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Dimension height ')),
                ('dimension_width', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Dimension width ')),
                ('dimension_length', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Dimension length')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso Bruto')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Eliminado')),
            ],
            options={
                'verbose_name': 'Dimension',
                'verbose_name_plural': 'Dimensiones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('last_modification', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Última modificación')),
                ('gross_weight', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Peso Bruto')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='box.dimension', verbose_name='Dimensión')),
            ],
            options={
                'verbose_name': 'Caja',
                'verbose_name_plural': 'Cajas',
                'ordering': ['-last_modification'],
            },
        ),
    ]
