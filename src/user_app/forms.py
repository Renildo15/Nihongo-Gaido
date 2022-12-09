from ast import arg
from django.forms import FileInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

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

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['id'] = 'old_p'
        self.fields['old_password'].widget.attrs['class'] = 'input'
        self.fields['new_password1'].widget.attrs['id'] = 'new_p'
        self.fields['new_password1'].widget.attrs['class'] = 'input'
        self.fields['new_password2'].widget.attrs['id'] = 'new_p2'
        self.fields['new_password2'].widget.attrs['class'] = 'input'
      

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']
        widgets = {
            "foto_perfil" : FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['foto_perfil'].widget.attrs = {'id':'selectedFile'}
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['telefone'].widget.attrs['id'] = 'telefone'
        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-data'})
        self.fields['data_nascimento'].widget.attrs['id'] = 'data'

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        exclude = ['password']

    def __init__(self, *args, **kwargs):
        super(ProfileUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['id'] = 'user'
        self.fields['first_name'].widget.attrs['id'] = 'f_name'
        self.fields['last_name'].widget.attrs['id'] = 'l_name'
        self.fields['email'].widget.attrs['id'] = 'email'