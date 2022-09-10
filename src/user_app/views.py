from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import RegisterUserForm, PasswordChangingForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def logar_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            messages.success(request,"Usuário logado com sucesso!")
            return redirect('/home/')
        else:
            messages.error(request,"Username ou senha incorretos! Tente novamente!")
            return redirect('/auth/login/')
    else:
        form_login = AuthenticationForm()

    context = {
        'form_login': form_login
    }
    return render(request, "login.html", context)
            

def cadastrar_user(request):
    if request.method == "POST":
        form_usuario = RegisterUserForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            username = form_usuario.cleaned_data['username']
            password = form_usuario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Cadastrado com sucesso!"))
            return redirect('/home/')
    else:
        form_usuario = RegisterUserForm()
    context = {
        'form_usuario': form_usuario
    }

    return render(request, 'cadastro.html', context)

@login_required(login_url='user:logar_user')
def deslogar_user(request):
    logout(request)
    messages.success(request, "Usuário deslogado com sucesso!")
    return redirect('/home/')