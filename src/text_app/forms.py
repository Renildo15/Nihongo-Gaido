from django import forms
from .models import Text, TextTraducao, TextWriting

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = '__all__'
        exclude = ['slug','criado_por']


class TextTraducaoForm(forms.ModelForm):
    class Meta:
        model = TextTraducao
        fields = '__all__'


class TextWritingForm(forms.ModelForm):
    class Meta:
        model = TextWriting
        fields = '__all__'