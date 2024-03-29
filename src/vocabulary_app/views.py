from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import *
from .forms import *
from utils.utils import pagination, verify_contains
# Create your views here.

@login_required(login_url='user:logar_user')
def word_list(request):
    categoria = Category.objects.filter(criado_por=request.user.id)

    if request.method == "POST":
        form_category = CategoryForm(request.POST)
        if form_category.is_valid():
            category = form_category.save(commit=False)
            category.criado_por = request.user
            category.save()
            messages.success(request, "Categoria adicionada com sucesso!")
            return HttpResponseRedirect(reverse('vocabulary:word_list'))
    else:
        form_category = CategoryForm()

    cat_form = form_category

    palavra_contains_query = request.GET.get('palavra_contains')
    categoria_contains_query = request.GET.get('categoria_contains')
    nivel_query = request.GET.get('select')
    parametro_limit = request.GET.get('limit', '12')
    parametro_page = request.GET.get('page', '1')

    word = Word.objects.filter(criado_por=request.user.id)
    word_by_category = word.values('categoria__nome').annotate(total=Count('categoria'))

    word = verify_contains(palavra_contains_query, categoria_contains_query, nivel_query, word)
    page = pagination(parametro_limit, word, parametro_page )

    context = {
        'words': page,
        'categorias': categoria,
        'cat_form': cat_form,
        'quantidade_por_pagina': ['12', '24', '48'],
        'qnt_pagina': parametro_limit,
        'word_by_category': word_by_category
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
def word_edit(request, slug):
    word = get_object_or_404(Word, slug=slug)
    form_word = WordForm(request.POST or None, instance=word)

    if form_word.is_valid():
        form_word.save()
        messages.success(request, "Palavra alterada com sucesso!")
        return redirect('vocabulary:word_list')

    context = {
        "form_vocabulary" : form_word
    }

    return render(request, "word_edit.html", context)

@login_required(login_url='user:logar_user')
def word_delete(request, slug):
    word = Word.objects.get(slug=slug)
    word.delete()
    messages.success(request, "Palavra deletada com sucesso!")
    return redirect(reverse("vocabulary:word_list"))


@login_required(login_url='user:logar_user')
def conjugation_list(request, slug):
    word = Word.objects.get(slug=slug)
    try:
        conjugations = Conjugation.objects.get(criado_por=request.user.id,slug=slug)
    except Conjugation.DoesNotExist:
        conjugations = None

    context = {
        "conjugations" : conjugations,
        "word": word
    }

    return render(request, "conjugation_list.html", context)

@login_required(login_url='user:logar_user')
def conjugation_create(request,slug):
    word = Word.objects.get(slug=slug)
    initial_dict = {
            "leitura" : word.leitura
    }
    if request.method == "POST":
        form_conjugation = ConjugationForm(request.POST or None, initial = initial_dict)
        if form_conjugation.is_valid():
            conjugation = form_conjugation.save(commit=False)
            conjugation.criado_por = request.user
            conjugation.palavra = word
            conjugation.save()
            messages.success(request,"Conjugação adicionada com sucesso!")
            return redirect(reverse('vocabulary:word_list'))
    else:
        form_conjugation = ConjugationForm(initial= initial_dict)

    context = {
        'form_conjugation': form_conjugation,
        'word': word
    }
    return render(request, "conjugation_form.html", context)


@login_required(login_url='user:logar_user')
def conjugation_edit(request, slug):
    conjugation = get_object_or_404(Conjugation, slug=slug)
    form_conjugation = ConjugationForm(request.POST or None, instance=conjugation)

    if form_conjugation.is_valid():
        form_conjugation.save()
        messages.success(request, "Conjugação alterada com sucesso!")
        return redirect('vocabulary:conjugation_list', slug=slug)

    context = {
        'form_conjugation': form_conjugation
    }

    return render(request, 'conjugation_edit.html', context)

