# Generated by Django 4.0.4 on 2022-10-08 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phrases_app', '0004_alter_grammar_phrase_grammar_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grammar_phrase',
            options={'ordering': ('traducao',), 'verbose_name_plural': 'Frases'},
        ),
    ]
