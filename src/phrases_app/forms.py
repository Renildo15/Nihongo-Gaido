from django import forms
from .models import Grammar_Phrase

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        readonly_fields = ('grammar_id',)
        fields = ('frase', 'traducao','explicacao', 'grammar_id')
        labels = {
            'frase': 'Frase',
            'traducao': 'Tradução',
            'explicacao': 'Explicação',
            'grammar_id': 'Estrutura',
        }
       

    def __init__(self, *args, **kwargs):
        super(GramarPhraseForm, self).__init__(*args, **kwargs)    
        #self.fields['grammar_id'].disabled = True