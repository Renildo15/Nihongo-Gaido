from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    telefone = models.CharField(null=True, blank=True, max_length=15)
    data_nascimento = models.DateField(null=True, blank=True)
    foto_perfil = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)


    def __str__(self):
        return self.user.first_name
