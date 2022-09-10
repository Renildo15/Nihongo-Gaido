from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Digite o seu email...', 'class': 'input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'nome', 'placeholder': 'Digite o seu nome...', 'class': 'input'}), label="Nome")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'sobrenome', 'placeholder': 'Digite o seu sobrenome...', 'class': 'input'}), label="Sobrenome")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        #help_texts = {
            #'username': None,
            #'email': None,
        #}

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Username...'
        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['id'] = 'senha'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha...'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['id'] = 'senha2'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar senha...'
        self.fields['password2'].widget.attrs['class'] = 'input'

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')