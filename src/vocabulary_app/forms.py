from django import forms
from .models import *


class WordForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = ('palavra', 'leitura','traducao','tipo', 'nivel', 'antonimo', 'grupo', 'categoria')
        exclude = ['slug','image','criado_por']
        labels = {
            'palavra': 'Palavra: ',
            'leitura': 'Leitura: ',
            'traducao': 'Tradução: ',
            'tipo': 'Tipo: ',
            'nivel': 'Nível: ',
            'antonimo': 'Antônimo: ',
            'grupo': 'Grupo: ',
            'categoria' :'Categoria: ',
        }

    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)    
        self.fields['tipo'].empty_label = "Selecione"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('nome',)
        labels = {
            'nome': 'Nome: '
        }




class ConjugationForm(forms.ModelForm):
    class Meta:
        model =  Conjugation
        fields = ('present','negative','past','te_form','volitional','potential','imperative','causative','conditional','passive','leitura')
        exclude = ['slug','criado_por', 'palavra']
        labels = {
            'present': 'Presente: ',
            'negative': 'Negativo',
            'past': 'Passado: ',
            'te_form': 'Forma-TE: ',
            'volitional': 'Volotiva: ',
            'potential': 'Potencial: ',
            'imperative': 'Imperativo: ',
            'causative': 'Causativa: ',
            'conditional': 'Condicional: ',
            'passive': 'Passiva: ',
            'leitura': 'Leitura: '
        }