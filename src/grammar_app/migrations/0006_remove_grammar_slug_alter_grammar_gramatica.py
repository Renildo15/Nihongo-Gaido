# Generated by Django 4.0.4 on 2022-12-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammar_app', '0005_grammar_slug_alter_grammar_gramatica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grammar',
            name='slug',
        ),
        migrations.AlterField(
            model_name='grammar',
            name='gramatica',
            field=models.CharField(max_length=200),
        ),
    ]
