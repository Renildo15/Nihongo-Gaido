from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from .forms import RegisterUserForm, PasswordChangingForm, ProfileForm, ProfileUserForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from .models import Profile

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

@login_required(login_url='user:logar_user')
def mudar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangingForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('/auth/mudar_senha_sucesso/')
    else:
        form_senha = PasswordChangingForm(request.user)
    context = {
        'form_senha': form_senha
    }
    return render(request, 'mudar_senha.html', context)

@login_required(login_url='user:logar_user')
def mudar_senha_sucesso(request):
    return render(request, 'mudar_senha_sucesso.html')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "senha/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/auth/reset_password_sent/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="senha/password_reset.html", context={"password_reset_form":password_reset_form})



@login_required(login_url='user:logar_user')
def profile_page(request):
    profile_info = Profile.objects.all()
    context = {
        "profile":profile_info
    }
    return render(request, "profile/profile.html", context)

@login_required(login_url='user:logar_user')
def profile_update_info(request):
    form_profile = ProfileForm(instance=request.user.profile)
    form_user = ProfileUserForm(instance=request.user)

    if request.method == "POST":
        form_profile = ProfileForm(request.POST or None, request.FILES, instance=request.user.profile)
        form_user = ProfileUserForm(request.POST or None, instance=request.user)
        if form_profile .is_valid() and form_user.is_valid():
            form_profile .save()
            form_user.save()
            return redirect("user:profile_page")
    context = {
        "form":form_profile ,
        "form_user":form_user
    }


    return render(request, "profile/profile_form.html", context)



