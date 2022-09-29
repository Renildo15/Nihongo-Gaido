from django.shortcuts import render, redirect, get_object_or_404, HttpResponse,reverse
from .models import Grammar_Phrase
from grammar_app.models import Grammar
from .forms import GramarPhraseForm
from django.contrib.auth.decorators import login_required
from grammar_app.encryption_util import *

# Create your views here.
@login_required(login_url='user:logar_user')
def phrase_list(request,pk):
    id = decrypt(pk)
    grammar_phrase = Grammar_Phrase.objects.filter(grammar_id=id)
    grs_phrase = grammar_phrase.values('id', 'frase', 'traducao', 'explicacao', 'grammar_id', 'criado_por')
    
    grp = []

    for i in grs_phrase:
        i['encrypt_key']=encrypt(i['id'])
        i['id'] = i['id']
        grp.append(i)
    print(grp)

    context = {
        'grammar_phrase': grp
    }
    return render(request, 'phrase_list.html', context)

@login_required(login_url='user:logar_user')
def phrase_view(request, pk):
    id = decrypt(pk)
    phrase = Grammar_Phrase.objects.get(pk=id)
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
    id = decrypt(pk)
    phrase = get_object_or_404(Grammar_Phrase, pk=id)
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
    id = decrypt(pk)
    phrase = Grammar_Phrase.objects.get(id = id)
    phrase.delete()
    return redirect('grammar:grammar_list')

