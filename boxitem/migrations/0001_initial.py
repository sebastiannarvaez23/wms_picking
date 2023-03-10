# Generated by Django 4.1.6 on 2023-03-09 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference', '0001_initial'),
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='box.box', verbose_name='Caja')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reference.reference', verbose_name='referencia')),
            ],
            options={
                'verbose_name': 'Referencia empacada',
                'verbose_name_plural': 'Referencias empacadas',
                'ordering': ['-id'],
            },
        ),
    ]
