from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .models import Grammar_Phrase
from grammar_app.models import Grammar
from .forms import GramarPhraseForm
from django.contrib.auth.decorators import login_required
from grammar_app.encryption_util import *
from django.contrib import  messages

# Create your views here.
@login_required(login_url='user:logar_user')
def phrase_list(request,pk):
    id = decrypt(pk)
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '3')
    grammar_phrase = Grammar_Phrase.objects.filter(grammar_id=id)
    grs_phrase = grammar_phrase.values('id', 'frase', 'traducao', 'explicacao', 'grammar_id', 'criado_por')
    
    grp = []

    for i in grs_phrase:
        i['encrypt_key']=encrypt(i['id'])
        i['id'] = i['id']
        grp.append(i)
    print(grp)

    if not(parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = "3"
    phrase_paginator = Paginator(grp, parametro_page)

    try:
        page = phrase_paginator.page(parametro_limit)
    except (EmptyPage, PageNotAnInteger):
        page = phrase_paginator.page(1)

    context = {
        'quantidade_por_pagina':['3','5','10','15'],
        'qnt_pagina': parametro_limit,
        'grammar_phrase': page
    }
    return render(request, 'phrase_list.html', context)

@login_required(login_url='user:logar_user')
def phrase_view(request, pk):
    id = decrypt(pk)
    phrase = Grammar_Phrase.objects.get(pk=id)
    context = {
        'phrase':phrase
    }

    return render(request, "phrase_view.html", context)

@login_required(login_url='user:logar_user')
def phrase_create(request):
    form = GramarPhraseForm()
    form.fields['grammar_id'].queryset = Grammar.objects.filter(criado_por = request.user)
    if request.method == 'POST':
        form_phrase = GramarPhraseForm(request.POST or None)
        if form_phrase.is_valid():
            grammar = form_phrase.save(commit=False)
            grammar.criado_por = request.user
            grammar.save()
            messages.success(request,"Frase adicionada com sucesso!")
            return redirect(reverse('phrase:add_phrase'))

    else:
        form_phrase = GramarPhraseForm()
    context = {
        'form_phrase': form_phrase,
        'form' : form
    }

    return render(request, 'phrase_form.html', context)

@login_required(login_url='user:logar_user')
def phrase_update(request, pk):
    #id = encrypt(pk)
    id = decrypt(pk)
    phrase = get_object_or_404(Grammar_Phrase, pk=id)
    form = GramarPhraseForm(request.POST or None, instance=phrase)
    if request.method == 'POST':
        form.fields['grammar_id'].queryset = Grammar.objects.filter(criado_por = request.user)
        print(phrase.grammar_id)
        if form.is_valid():
            form.save()
            ##TODO:Fazer com que seja redirecionadp para a tela Phrase list
            return redirect('grammar:grammar_list')

    context = {
        "form": form
    }

    return render(request, 'phrase_form.html', context)
    
@login_required(login_url='user:logar_user')
def phrase_delete(request, pk):
    id = decrypt(pk)
    phrase = Grammar_Phrase.objects.get(id = id)
    phrase.delete()
    messages.success(request,"Frase deletada com sucesso!")
    return redirect('grammar:grammar_list')

