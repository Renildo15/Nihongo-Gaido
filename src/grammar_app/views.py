from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Grammar
from .forms import GrammarForm
from django.contrib import messages
# Create your views here.
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='user:logar_user')
def grammar_list(request):
    grammar_contains_query = request.GET.get('grammar_contains')
    estrutura_contains_query = request.GET.get('estrutura_contains')
    parametro_page = request.GET.get('page', '1')
    parametro_limit = request.GET.get('limit', '15')
    nivel_query = request.GET.get('select')

    grammar = Grammar.objects.filter(criado_por=request.user.id)

    if grammar_contains_query:
        grammar = grammar.filter(gramatica__icontains=grammar_contains_query)
    elif estrutura_contains_query:
        grammar = grammar.filter(estrutura__icontains=estrutura_contains_query)
    elif nivel_query:
        grammar = grammar.filter(nivel__icontains=nivel_query)

    if not parametro_limit.isdigit() or int(parametro_limit) <= 0:
        parametro_limit = '15'

    grammar_paginator = Paginator(grammar, parametro_limit)

    try:
        page = grammar_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = grammar_paginator.page(1)

    context = {
        'quantidade_por_pagina': ['15', '25', '35', '45'],
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
    grammar = get_object_or_404(Grammar, pk=pk)
    form_grammar = GrammarForm(request.POST or None, instance=grammar)

    if form_grammar.is_valid():
        form_grammar.save()
        messages.success(request,"Gramática alterada com sucesso!")
        return redirect('grammar:grammar_list')

    context = {
        "form_grammar":form_grammar
    }
    return render(request, 'grammar_edit.html', context)

@login_required(login_url='user:logar_user')
def grammar_delete(request, pk):
    grammar = Grammar.objects.get(id = pk)
    grammar.delete()
    messages.success(request, "Grámatica deletada com sucesso!")
    return redirect(reverse('grammar:grammar_list'))


