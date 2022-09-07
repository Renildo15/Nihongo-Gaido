from django.db import models
# Create your models here.

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
    def __str__(self):
        return self.gramatica