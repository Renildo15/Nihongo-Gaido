from django.shortcuts import render, redirect, reverse
from .forms import TextForm,TextTraducaoForm,TextWriting
from .models import Text,TextTraducao, TextWriting
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='user:logar_user')
def text_options(request):
    return render(request, "text_options.html")
@login_required(login_url='user:logar_user')
def text_list(request):
    texts = Text.objects.filter(criado_por=request.user.id)
    context = {
        "texts": texts
    }
    return render(request, 'text_list.html', context)

@login_required(login_url='user:logar_user')
def text_create(request):
    if request.method == "POST":
         text_form = TextForm(request.POST or None)
         
         if text_form.is_valid():
            text = text_form.save(commit=False)
            text.criado_por = request.user
            text.save()
            messages.success(request,"Texto adicionado com sucesso!")
            return redirect(reverse('text:add_text'))
    else:
        text_form = TextForm()
    context = {
        "text_form":text_form
    }
    return render(request, 'text_form.html', context)
