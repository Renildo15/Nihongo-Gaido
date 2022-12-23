# Generated by Django 4.0.4 on 2022-11-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('nome',), 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterField(
            model_name='word',
            name='antonimo',
            field=models.CharField(blank=True, default='---', max_length=20, null=True),
        ),
    ]
