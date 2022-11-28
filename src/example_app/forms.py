from django import forms
from .models import Example


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = '__all__'