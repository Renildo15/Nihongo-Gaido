from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import RegisterUserForm, PasswordChangingForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages


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
            
