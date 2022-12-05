from django import forms
from .models import Grammar_Phrase

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        fields = ('frase', 'traducao','explicacao', 'grammar_id')
        labels = {
            'frase': 'Frase: ',
            'traducao': 'Tradução: ',
            'explicacao': 'Explicação: ',
        }
        
        widgets = {
            'grammar_id': forms.HiddenInput()
        }
     

    def __init__(self, *args, **kwargs):
        super(GramarPhraseForm, self).__init__(*args, **kwargs)    
        #self.fields['grammar_id'].disabled = True
        self.fields['grammar_id'].empty_label = "Selecione"
        self.fields['grammar_id'].label = ''