# Generated by Django 4.0.4 on 2022-11-26 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Nomes',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palavra', models.CharField(max_length=20)),
                ('leitura', models.CharField(max_length=20, unique=True)),
                ('traducao', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[('Verbo', 'Verbo'), ('Adjetivo-I', 'Adjetivo-I'), ('Adjetivo-NA', 'Adjetivo-NA'), ('Substantivo', 'Substantivo')], max_length=20)),
                ('nivel', models.CharField(choices=[('N5', 'N5'), ('N4', 'N4'), ('N3', 'N3'), ('N2', 'N2'), ('N1', 'N1'), ('UNKNOW', 'UNKNOW')], max_length=6)),
                ('antonimo', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('imagem', models.ImageField(blank=True, default='profile.png', null=True, upload_to='')),
                ('grupo', models.CharField(blank=True, choices=[('Grupo 1', 'Grupo 1 '), ('Grupo 2 ', 'Grupo 2'), ('Grupo 3', 'Grupo 3'), ('Não é verbo', 'Não é verbo')], max_length=20, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vocabulary_app.category')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Palavras',
                'ordering': ('palavra',),
            },
        ),
        migrations.CreateModel(
            name='Conjugation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.CharField(blank=True, max_length=20, null=True)),
                ('negative', models.CharField(blank=True, max_length=20, null=True)),
                ('past', models.CharField(blank=True, max_length=20, null=True)),
                ('te_form', models.CharField(blank=True, max_length=20, null=True)),
                ('volitional', models.CharField(blank=True, max_length=20, null=True)),
                ('potential', models.CharField(blank=True, max_length=20, null=True)),
                ('imperative', models.CharField(blank=True, max_length=20, null=True)),
                ('causative', models.CharField(blank=True, max_length=20, null=True)),
                ('conditional', models.CharField(blank=True, max_length=20, null=True)),
                ('passive', models.CharField(blank=True, max_length=20, null=True)),
                ('leitura', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('palavra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vocabulary_app.word')),
            ],
            options={
                'verbose_name_plural': 'Conjugações',
                'ordering': ('palavra',),
            },
        ),
    ]