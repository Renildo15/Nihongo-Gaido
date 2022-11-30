from django import forms
from .models import Example


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ('frase', 'traducao', 'anotacao')
        labels = {
            'frase': 'Frase: ',
            'traducao': 'Tradução: ',
            'anotacao': 'Anotações'
        }
        exclude = ['slug','criado_por', 'palavra','leitura']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['anotacao'].widget = forms.Textarea(attrs={'style':'width:100%; border-radius:10px; padding:10px;'})