from django.shortcuts import render, redirect, get_object_or_404
from .models import Grammar_Phrase
from .forms import GramarPhraseForm

# Create your views here.
def phrase_list(request,pk):
    ##grammar_id = Grammar.objects.only('id').get(id=pk).id
    grammar_phrase = Grammar_Phrase.objects.filter(id=pk)
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

def phrase_delete(request, pk):
    phrase = Grammar_Phrase.objects.get(id = pk)
    phrase.delete()
    return redirect('grammar:phrases_list')

