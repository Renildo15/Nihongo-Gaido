from urllib import request
from django import forms
from .models import Grammar

class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = ('gramatica', 'estrutura', 'nivel')
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    

