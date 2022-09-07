from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Grammar, Grammar_Phrase
from .forms import GramarPhraseForm, GrammarForm
# Create your views here.

def grammar_list(request):
    grammar = Grammar.objects.all()
    context = {
        'grammar': grammar,
    }

    return render(request, 'grammar_list.html', context)



def phrase_list(request,pk):
    grammar_phrase = Grammar_Phrase.objects.filter(id=pk)
    context = {
        'grammar_phrase': grammar_phrase
    }
    return render(request, 'phrase_list.html', context)



def grammar_create(request):
    form_Grammar = GrammarForm(request.POST or None)
    if request.method == 'POST':
        if form_Grammar.is_valid():
            form_Grammar.save()
            return redirect('grammar:grammar_list')
    context = {
        'form_grammar': form_Grammar,
    }

    return render(request, 'grammar_form.html', context)


def phrase_create(request):
    form_phrase = GramarPhraseForm(request.POST or None)
    if request.method == 'POST':
        if form_phrase.is_valid():
            form_phrase.save()
            return redirect('grammar:grammar_list')
    context = {
        'form_phrase': form_phrase,
    }

    return render(request, 'phrase_form.html', context)

def grammar_update(request, pk):
    grammar = get_object_or_404(Grammar, pk=pk)
    form_grammar = GrammarForm(request.POST or None, instance=grammar)

    if form_grammar.is_valid():
        form_grammar.save()
        return redirect('grammar:grammar_list')
    
    context = {
        "form_grammar":form_grammar
    }
    return render(request, 'grammar_form.html', context)


def phrase_update(request,pk):
    phrase = get_object_or_404(Grammar_Phrase, pk=pk)
    form_phrase = GramarPhraseForm(request.POST or None, instance=phrase)

    if form_phrase.is_valid():
        form_phrase.save()
        return redirect('grammar:phrases_list')

    context = {
        "form_phrase": form_phrase
    }

    return render(request, 'phrase_form.html', context)



def grammar_delete(request, pk):
    grammar = Grammar.objects.get(id = pk)
    grammar.delete()
    return redirect('grammar:grammar_list')


def phrase_delete(request, pk):
    phrase = Grammar_Phrase.objects.get(id = pk)
    phrase.delete()
    return redirect('grammar:phrases_list')
