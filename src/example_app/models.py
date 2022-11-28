from django.db import models
from django.contrib.auth import settings
from django.template.defaultfilters import slugify
from vocabulary_app.models import Word
# Create your models here.

class Example(models.Model):
    frase = models.CharField(max_length=200)
    leitura = models.CharField(max_length=200, unique=True)
    traducao = models.CharField(max_length=200)
    anotacao = models.TextField(max_length=500, null=True, blank=True)
    palavra = models.ForeignKey(Word, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Exemplos"
        ordering = ('frase',)

    def __str__(self):
        return self.frase

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.leitura)
        return super().save(*args,**kwargs)

