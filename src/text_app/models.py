from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth import settings

# Create your models here.
class Text(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    texto = RichTextField()
    comentario = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Textos"
        ordering = ('titulo', )

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)
  


class TextTraducao(models.Model):
    titulo_traducao = models.CharField(max_length=200, unique=True)
    texto_traducao = RichTextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    text_id = models.ForeignKey(Text,on_delete=models.CASCADE,blank=True, null=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Textos-Traduzidos"
        ordering = ('titulo_traducao', )

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo_traducao)
        return super().save(*args, **kwargs)



class TextWriting(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    texto = RichTextField()
    comentario = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Textos-Escritos"
        ordering = ('titulo', )

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)

