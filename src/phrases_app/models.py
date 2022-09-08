from django.db import models
from grammar_app.models import Grammar
# Create your models here.

class Grammar_Phrase(models.Model):
    frase = models.CharField(max_length=200)
    traducao = models.CharField(max_length=200)
    explicacao = models.CharField(max_length=300, blank=True, null=True)
    grammar_id = models.ForeignKey(Grammar, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.frase

