from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

@login_required(login_url='user:logar_user')
def word_list(request):
    word = Word.objects.filter(criado_por=request.user.id)
    categoria = Category.objects.filter(criado_por=request.user.id)

    context = {
        "words": word,
        "categorias": categoria
    }

    return render(request, "word_list.html", context)

@login_required(login_url='user:logar_user')
def word_create(request):
    if request.method == "POST":
        form_word = WordForm(request.POST or None)
        if form_word.is_valid():
            word = form_word.save(commit=False)
            word.criado_por = request.user
            word.save()
            messages.success(request,"Palavra adicionada com sucesso!")
            return redirect(reverse('vocabulary:add_word'))

    else:
         form_word = WordForm()

    context = {
        "form_vocabulary": form_word
    }

    return render(request, "word_form.html", context)


@login_required(login_url='user:logar_user')
def conjugation_list(request, slug):
    try:
        conjugations = Conjugation.objects.get(criado_por=request.user.id,slug=slug)
    except Conjugation.DoesNotExist:
        conjugations = None

    context = {
        "conjugations" : conjugations
    }

    return render(request, "conjugation_list.html", context)