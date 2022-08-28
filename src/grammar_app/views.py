from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Grammar, Grammar_Phrase
from .forms import GramarPhraseForm, GrammarForm
# Create your views here.

def index(request):
    grammar = Grammar.objects.all()
    grammar_phrase = Grammar_Phrase.objects.all()
    context = {
        'grammar': grammar,
        'grammar_Phrase': grammar_phrase
    }

    return render(request, 'grammar_list.html', context)

def grammar_create(request):
    form_Grammar = GrammarForm(request.POST or None)
    form_phrase = GramarPhraseForm(request.POST or None)
    if form_Grammar.is_valid() and form_phrase.is_valid():
        form_Grammar.save()
        form_phrase.save()
        return redirect('grammar:index')
    context = {
        'form_grammar': form_Grammar,
        'form_phrase': form_phrase
    }

    return render(request, 'grammar_form.html', context)
