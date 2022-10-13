from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(null=True, blank=True, max_length=15)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)


    def __str__(self):
        return self.user.first_name
