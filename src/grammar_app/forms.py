from dataclasses import field
from pyexpat import model
from django import forms
from .models import Grammar, Grammar_Phrase

class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = '__all__'

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        fields = '__all__'