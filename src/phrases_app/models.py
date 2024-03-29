from django.db import models
from grammar_app.models import Grammar
from django.contrib.auth import settings
from django.template.defaultfilters import slugify
# Create your models here.

class Grammar_Phrase(models.Model):
    frase = models.CharField(max_length=200, unique=True)
    traducao = models.CharField(max_length=200)
    observacao = models.TextField(max_length=300, blank=True, null=True)
    grammar_id = models.ForeignKey(Grammar, on_delete=models.CASCADE, null=True, blank=True, related_name="Grammar_Phrase")
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    

    class Meta:
        verbose_name_plural = "Frases"
        ordering = ('traducao', )

    def __str__(self):
        return self.frase
        

