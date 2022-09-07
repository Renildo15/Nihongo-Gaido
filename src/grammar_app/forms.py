from dataclasses import field
from pyexpat import model
from django import forms
from .models import Grammar, Grammar_Phrase

class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GrammarForm, self).__init__(*args, **kwargs)
        self.fields['frases'].empty_label = "Selecione"
        self.fields['frases'].required = False
        self.fields['nivel'].empty_label = "Selecione"

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        fields = '__all__'