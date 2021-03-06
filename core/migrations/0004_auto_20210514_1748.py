# Generated by Django 3.2 on 2021-05-14 20:48

import core.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão')),
            ],
            options={
                'verbose_name': 'Profissão',
                'verbose_name_plural': 'Profissões',
            },
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='instrgram',
            new_name='instagram',
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('depoimento', models.TextField(max_length=200, verbose_name='Depoimento')),
                ('imagem', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
                ('nota', models.IntegerField(verbose_name='Nota')),
                ('profissao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profissao', verbose_name='Profissão')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
