from django.db import models
from django.contrib.auth import settings
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ('nome', )

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save(*args,**kwargs)


class Word(models.Model):

    tipo_choice =(
        ("Verbo", "Verbo"),
        ("Adjetivo-I", "Adjetivo-I"),
        ("Adjetivo-NA", "Adjetivo-NA"),
        ("Substantivo", "Substantivo")
    )

    nivel_choices = (
        ('N5','N5'),
        ('N4','N4'),
        ('N3','N3'),
        ('N2','N2'),
        ('N1','N1'),
        ('UNKNOW','UNKNOW')
    )

    grupo_choice = (
        ("Grupo 1", "Grupo 1 "),
        ("Grupo 2 ", "Grupo 2"),
        ("Grupo 3", "Grupo 3"),
        ("Não é verbo", "Não é verbo")
    )
    palavra = models.CharField(max_length=20)
    leitura = models.CharField(max_length=20, unique=True)
    traducao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices= tipo_choice)
    nivel = models.CharField(max_length=6, choices=nivel_choices)
    antonimo = models.CharField(max_length=200, blank=True, null=True, default="---")
    slug = models.SlugField(unique=True, blank=True, null=True)
    imagem = models.ImageField(default="profile.png", null=True, blank=True)
    grupo = models.CharField(max_length=20, choices=grupo_choice, blank=True, null=True)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Palavras"
        ordering = ('palavra',)

    def __str__(self):
        return self.palavra
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.leitura)
        return super().save(*args, **kwargs)


class Conjugation(models.Model):
    palavra = models.OneToOneField(Word, on_delete=models.CASCADE, blank=True, null=True)
    present = models.CharField(max_length=20, blank=True, null=True)
    negative = models.CharField(max_length=20, blank=True, null=True)
    past = models.CharField(max_length=20, blank=True, null=True)
    te_form = models.CharField(max_length=20, blank=True, null=True)
    volitional = models.CharField(max_length=20, blank=True, null=True)
    potential = models.CharField(max_length=20, blank=True, null=True)
    imperative = models.CharField(max_length=20, blank=True, null=True)
    causative = models.CharField(max_length=20, blank=True, null=True)
    conditional = models.CharField(max_length=20, blank=True, null=True)
    passive = models.CharField(max_length=20, blank=True, null=True)
    leitura = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Conjugações"
        ordering = ("palavra",)

    def __str__(self):
        return self.present

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.leitura)
        return super().save(*args, **kwargs)