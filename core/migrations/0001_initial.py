# Generated by Django 4.0.5 on 2022-07-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enderecinho', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=7)),
                ('cidade_estado', models.CharField(max_length=128)),
                ('bairro', models.CharField(max_length=64)),
                ('logradouro', models.CharField(max_length=1024)),
                ('edificio', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
