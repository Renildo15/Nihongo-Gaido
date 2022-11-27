from django import forms
from .models import *


class WordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ('palavra','traducao','tipo', 'nivel', 'antonimo', 'grupo', 'categoria')
        exclude = ['slug','image','criado_por']
        labels = {
            'palavra': 'Palavra: ',
            'traducao': 'Tradução: ',
            'tipo': 'Tipo: ',
            'nivel': 'Nível: ',
            'antonimo': 'Antônimo: ',
            'grupo': 'Grupo: ',
            'categoria' :'Categotia: ',
        }
