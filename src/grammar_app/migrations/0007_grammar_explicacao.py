# Generated by Django 4.1.4 on 2023-04-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammar_app', '0006_remove_grammar_slug_alter_grammar_gramatica'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammar',
            name='explicacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
