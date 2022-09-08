from django import forms
from .models import Grammar_Phrase

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        fields = ('frase', 'traducao','explicacao', 'grammar_id')
        labels = {
            'frase': 'Frase',
            'traducao': 'Tradução',
            'explicacao': 'Explicação',
            'grammar_id': 'Estrutura',
        }