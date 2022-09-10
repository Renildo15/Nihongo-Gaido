from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'nome'}), label="Nome")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'sobrenome'}), label="Sobrenome")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['password1'].widget.attrs['id'] = 'senha'
        self.fields['password2'].widget.attrs['id'] = 'senha2'

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')