# Generated by Django 4.0.4 on 2022-09-29 18:41

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('grammar_app', '0002_alter_grammar_options_grammar_criado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grammar',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False),
        ),
    ]