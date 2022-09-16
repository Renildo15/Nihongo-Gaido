from django import forms
from .models import Grammar

class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = '__all__'

        
    

