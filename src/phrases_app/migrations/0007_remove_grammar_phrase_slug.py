# Generated by Django 4.0.4 on 2022-12-01 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phrases_app', '0006_grammar_phrase_slug_alter_grammar_phrase_frase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grammar_phrase',
            name='slug',
        ),
    ]