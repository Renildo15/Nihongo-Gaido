from django import forms
from .models import Grammar

class GrammarForm(forms.ModelForm):
    class Meta:
        model = Grammar
        fields = "__all__"
        labels = {
            'gramatica': 'Gramática: ',
            'estrutura': 'Estrutura: ',
            'nivel': 'Nível: ',
            'explicacao': 'Explicação: '
        }

        widgets = {
            'explicacao': forms.Textarea(attrs={'class':'form-control', 'style':'width:600px;'}),
        }
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['criado_por'].widget = forms.HiddenInput()
        self.fields['criado_por'].label = ''
        
        
    

