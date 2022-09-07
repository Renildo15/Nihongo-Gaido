from django.db import models

# Create your models here.

class Grammar_Phrase(models.Model):
    frase = models.CharField(max_length=200)
    traducao = models.CharField(max_length=200)
    explicacao = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.frase

class Grammar(models.Model):
    nivel_choices = (
        ('N5','N5'),
        ('N4','N4'),
        ('N3','N3'),
        ('N2','N2'),
        ('N1','N1'),
        ('UNKNOW','UNKNOW')
    )

    gramatica = models.CharField(max_length=200)
    estrutura = models.CharField(max_length=200)
    nivel = models.CharField(max_length=6, choices=nivel_choices)
    frases = models.ForeignKey(Grammar_Phrase, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.gramatica