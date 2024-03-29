from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.urls import reverse
from .models import Grammar_Phrase
from grammar_app.models import Grammar
from .forms import GramarPhraseForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from utils.utils import pagination

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
            messages.success(request,"Frase alterada com sucesso!")
            return redirect('grammar:grammar_detail', phrase.grammar_id.pk)

    context = {
        "form": form
    }

    return render(request, 'phrase_edit.html', context)
    
@login_required(login_url='user:logar_user')
def phrase_delete(request, pk):
    phrase = Grammar_Phrase.objects.get(id = pk)
    phrase.delete()
    messages.success(request,"Frase deletada com sucesso!")
    return redirect('grammar:grammar_list')

