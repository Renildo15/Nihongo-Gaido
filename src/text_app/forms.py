from django import forms
from .models import Text, TextTraducao, TextWriting
from ckeditor.fields import RichTextField

class TextForm(forms.ModelForm):
    texto = RichTextField()
    class Meta:
        model = Text
        fields = ('titulo', 'texto', 'comentario')
        exclude = ['slug','criado_por']

        labels={
            'titulo':'Título:',
            'texto':'Texto:',
            'comentario': 'Comentário:'
        }

        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control', 'style':'width:600px;'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comentario'].widget = forms.Textarea(attrs={'style':'width:100%; border-radius:10px; padding:10px;'})

class TextTraducaoForm(forms.ModelForm):
    texto = RichTextField()
    class Meta:
        model = TextTraducao
        fields = ('titulo_traducao','texto_traducao',)
        exclude = ['slug','criado_por','text_id']

        labels={
            'titulo_traducao': '',
            'texto_traducao':'Traducão:'
        }

        widgets = {
            'texto_traducao':forms.Textarea(attrs={'class':'form-control', 'style':'width:600px;'}),
            'titulo_traducao': forms.HiddenInput()
        }

       

class TextWritingForm(forms.ModelForm):
    class Meta:
        model = TextWriting
        fields = '__all__'