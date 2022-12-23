from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .models import Grammar_Phrase
from grammar_app.models import Grammar
from .forms import GramarPhraseForm
from django.contrib.auth.decorators import login_required
from django.contrib import  messages

# Create your views here.
@login_required(login_url='user:logar_user')
def phrase_list(request,pk):
    paramentro_page = request.GET.get('page', '1')
    paramentro_limit = request.GET.get('limit', '3')
    grammar_phrase = Grammar_Phrase.objects.filter(criado_por= request.user.id, grammar_id=pk)
    grammar = get_object_or_404(Grammar, pk=pk)
    if not( paramentro_limit.isdigit() and int( paramentro_limit) > 0):
         paramentro_limit = "3"
    phrase_paginator = Paginator(grammar_phrase, paramentro_limit)

    try:
        page = phrase_paginator.page(paramentro_page)
    except (EmptyPage, PageNotAnInteger):
        page = phrase_paginator.page(1)

    context = {
        'quantidade_por_pagina':['3','5','10','15'],
        'qnt_pagina':  paramentro_limit,
        'grammar_phrase': page,
        'id_grammar': pk,
        'g': grammar
    }
    return render(request, 'phrase_list.html', context)

@login_required(login_url='user:logar_user')
def phrase_view(request, pk):
    phrase = Grammar_Phrase.objects.get(pk=pk)
    context = {
        'phrase':phrase
    }

    return render(request, "phrase_view.html", context)

@login_required(login_url='user:logar_user')
def phrase_create(request, pk):
    form = GramarPhraseForm()
    g = get_object_or_404(Grammar, pk=pk)
    form.fields['grammar_id'].queryset = Grammar.objects.filter(criado_por = request.user)
    if request.method == 'POST':
        form_phrase = GramarPhraseForm(request.POST or None)
        if form_phrase.is_valid():
            grammar = form_phrase.save(commit=False)
            grammar.grammar_id = g
            grammar.criado_por = request.user
            grammar.save()
            messages.success(request,"Frase adicionada com sucesso!")
            return redirect(reverse('phrase:add_phrase', kwargs={'pk': pk}))

    else:
        form_phrase = GramarPhraseForm()
    context = {
        'form_phrase': form_phrase,
        'form' : form,
        'g': g
    }

    return render(request, 'phrase_form.html', context)

@login_required(login_url='user:logar_user')
def phrase_update(request, pk):
    phrase = get_object_or_404(Grammar_Phrase, pk=pk)
    form = GramarPhraseForm(request.POST or None, instance=phrase)
    if request.method == 'POST':
        form.fields['grammar_id'].queryset = Grammar.objects.filter(criado_por = request.user)
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
    phrase = Grammar_Phrase.objects.get(id = pk)
    phrase.delete()
    messages.success(request,"Frase deletada com sucesso!")
    return redirect('grammar:grammar_list')

