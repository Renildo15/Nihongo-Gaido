from django import forms
from .models import Grammar_Phrase

class GramarPhraseForm(forms.ModelForm):
    class Meta:
        model = Grammar_Phrase
        fields = '__all__'