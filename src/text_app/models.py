from django.db import models
from django.contrib.auth import settings

# Create your models here.
class Text(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    texto = models.TextField(max_length=900)
    comentario = models.TextField(max_length=900)
    slug = models.SlugField(unique=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Textos"
        ordering = ('titulo', )

    def __str__(self):
        return self.titulo
  


class TextTraducao(models.Model):
    titulo_traducao = models.CharField(max_length=200, unique=True)
    texto_traducao = models.TextField(max_length=900)
    slug = models.SlugField(unique=True)
    text_id = models.ForeignKey(Text,on_delete=models.CASCADE,blank=True, null=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Textos-Traduzidos"
        ordering = ('titulo', )

    def __str__(self):
        return self.titulo

