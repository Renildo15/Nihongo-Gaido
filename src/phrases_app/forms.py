from django import forms
from .models import Grammar_Phrase

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        fields = ('frase', 'traducao','observacao', 'grammar_id')
        labels = {
            'frase': 'Frase: ',
            'traducao': 'Tradução: ',
            'observacao': 'Observação: ',
        }
        
        widgets = {
            'observacao': forms.Textarea(attrs={'class':'form-control', 'style':'width:600px;'}),
            'grammar_id': forms.HiddenInput()
        }


    def __init__(self, *args, **kwargs):
        super(GramarPhraseForm, self).__init__(*args, **kwargs)    
        self.fields['grammar_id'].empty_label = "Selecione"
        self.fields['grammar_id'].label = ''