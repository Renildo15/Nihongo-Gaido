# Generated by Django 4.0.4 on 2022-12-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_alter_profile_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]