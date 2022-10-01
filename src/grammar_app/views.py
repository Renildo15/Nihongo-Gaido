from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Grammar
from .forms import GrammarForm
from .encryption_util import *
from django.contrib import  messages
# Create your views here.
@login_required(login_url='user:logar_user')
def grammar_list(request):
    grammar = Grammar.objects.filter(criado_por=request.user.id)
    grs = grammar.values('id', 'gramatica', 'estrutura', 'nivel','criado_por')
    g = []
    for i in grs:
        i['encrypt_key']=encrypt(i['id'])
        i['id'] = i['id']
        g.append(i)
    context = {
        'grammar': g,
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
            messages.add_message(request, messages.SUCCESS, "Gramática adicionada com sucesso!")
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
    messages.add_message(request, messages.SUCCESS, "Apagado com sucesso!!")
    return redirect(reverse('grammar:grammar_list'))


