from django.shortcuts import render, redirect, get_object_or_404, HttpResponse,reverse
from .models import Grammar_Phrase
from grammar_app.models import Grammar
from .forms import GramarPhraseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='user:logar_user')
def phrase_list(request,pk):
    #TODO tentar corrigir a parte de segurança
    grammar_phrase = Grammar_Phrase.objects.filter(grammar_id=pk)
    context = {
        'grammar_phrase': grammar_phrase
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
def phrase_create(request):
    form = GramarPhraseForm()
    form.fields['grammar_id'].queryset = Grammar.objects.filter(criado_por = request.user)
    if request.method == 'POST':
        form_phrase = GramarPhraseForm(request.POST or None)
        if form_phrase.is_valid():
            form_phrase.save()
            return redirect('grammar:grammar_list')

    else:
        form_phrase = GramarPhraseForm()
    context = {
        'form_phrase': form_phrase,
        'form' : form
    }

    return render(request, 'phrase_form.html', context)

@login_required(login_url='user:logar_user')
def phrase_update(request, pk):
    phrase = get_object_or_404(Grammar_Phrase, pk=pk)
    form = GramarPhraseForm(request.POST or None, instance=phrase)
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
    phrase = Grammar_Phrase.objects.get(id = pk)
    phrase.delete()
    return redirect('grammar:grammar_list')

