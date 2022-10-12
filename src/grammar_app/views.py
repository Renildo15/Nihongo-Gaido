from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Grammar
from .forms import GrammarForm
from .encryption_util import *
from django.contrib import  messages
# Create your views here.
@login_required(login_url='user:logar_user')
def grammar_list(request):
    grammar_contains_query = request.GET.get('grammar_contains')
    estrutura_contains_query = request.GET.get('estrutura_contains')
    nivel_contains_query = request.GET.get('nivel_contains')
    paramentro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '3')

    if grammar_contains_query != "" and grammar_contains_query is not None:
        grammar = Grammar.objects.filter(criado_por=request.user.id, gramatica__icontains = grammar_contains_query)
        grs = grammar.values('id', 'gramatica', 'estrutura', 'nivel','criado_por')
        g = []
        for i in grs:
            i['encrypt_key']=encrypt(i['id'])
            i['id'] = i['id']
            g.append(i)
        if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '3'

        grammar_paginator = Paginator(g, parametro_limit)

        try:
            page = grammar_paginator.page(paramentro_page)
        except (EmptyPage, PageNotAnInteger):
            page = grammar_paginator.page(1)
    else:
        grammar = Grammar.objects.filter(criado_por=request.user.id)
        grs = grammar.values('id', 'gramatica', 'estrutura', 'nivel','criado_por')
        g = []
        for i in grs:
            i['encrypt_key']=encrypt(i['id'])
            i['id'] = i['id']
            g.append(i)
        if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = '3'

        grammar_paginator = Paginator(g, parametro_limit)

        try:
            page = grammar_paginator.page(paramentro_page)
        except (EmptyPage, PageNotAnInteger):
            page = grammar_paginator.page(1)
    context = {
        'quantidade_por_pagina':['3','5','10','15'],
        'qnt_pagina': parametro_limit,
        'grammar': page,
    }

    
    return render(request, 'grammar_list.html', context)




@login_required(login_url='user:logar_user')
def grammar_create(request):
    if request.method == 'POST':
        form_Grammar = GrammarForm(request.POST or None)
        if form_Grammar.is_valid():
            grammar = form_Grammar.save(commit=False)
            grammar.criado_por = request.user
            grammar.save()
            messages.success(request,"Gramática adicionada com sucesso!")
            return redirect(reverse('grammar:add_grammar'))
    else:
        form_Grammar = GrammarForm()

    context = {
        'form_grammar': form_Grammar,
    }
   
    return render(request, 'grammar_form.html', context)

@login_required(login_url='user:logar_user')
def grammar_update(request, pk):
    id = decrypt(pk)
    grammar = get_object_or_404(Grammar, pk=id)
    form_grammar = GrammarForm(request.POST or None, instance=grammar)

    if form_grammar.is_valid():
        form_grammar.save()
        return redirect('grammar:grammar_list')
    
    context = {
        "form_grammar":form_grammar
    }
    return render(request, 'grammar_form.html', context)

@login_required(login_url='user:logar_user')
def grammar_delete(request, pk):
    id = decrypt(pk)
    grammar = Grammar.objects.get(id = id)
    grammar.delete()
    messages.success(request, "Grámatica deletada com sucesso!")
    return redirect(reverse('grammar:grammar_list'))


