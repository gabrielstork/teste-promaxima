# Generated by Django 4.0.3 on 2022-03-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GasolinaComum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('valor_unitario', models.DecimalField(decimal_places=3, max_digits=5)),
                ('valor_ultima_venda', models.DecimalField(decimal_places=3, max_digits=5)),
                ('tempo_ultima_venda', models.CharField(max_length=50)),
                ('contribuinte', models.CharField(max_length=200)),
                ('codigo', models.PositiveIntegerField()),
                ('raspagem', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Gasolina Comum',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
