from django.shortcuts import render, redirect, get_object_or_404, HttpResponse,reverse
from .models import Grammar_Phrase
from grammar_app.models import Grammar
from grammar_app.forms import GrammarForm
from .forms import GramarPhraseForm

# Create your views here.
def phrase_list(request,pk):
    ##grammar_id = Grammar.objects.only('id').get(id=pk).id
    grammar_phrase = Grammar_Phrase.objects.filter(grammar_id=pk)
    context = {
        'grammar_phrase': grammar_phrase
    }
    return render(request, 'phrase_list.html', context)

def phrase_create(request):
    if request.method == 'POST':
        form_phrase = GramarPhraseForm(request.POST or None)
        if form_phrase.is_valid():
            form_phrase.save()
            return redirect('grammar:grammar_list')

    else:
        form_phrase = GramarPhraseForm()
    context = {
        'form_phrase': form_phrase,
    }

    return render(request, 'phrase_form.html', context)


def phrase_update(request, pk):
    phrase = get_object_or_404(Grammar_Phrase, pk=pk)
    form_phrase = GramarPhraseForm(request.POST or None, instance=phrase)
    print(phrase.grammar_id)
    if form_phrase.is_valid():
        form_phrase.save()
        ##TODO:Fazer com que seja redirecionadp para a tela Phrase list
        return redirect('grammar:grammar_list')

    context = {
        "form_phrase": form_phrase
    }

    return render(request, 'phrase_form.html', context)

def phrase_delete(request, pk):
    phrase = Grammar_Phrase.objects.get(id = pk)
    phrase.delete()
    return redirect('grammar:grammar_list')

