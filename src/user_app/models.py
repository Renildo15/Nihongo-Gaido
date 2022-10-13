from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    telefone = models.CharField(null=True, blank=True, max_length=15)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)

    def __str__(self):
        return self.user.name
