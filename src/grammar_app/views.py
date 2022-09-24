from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Grammar
from .forms import GrammarForm
# Create your views here.
@login_required(login_url='user:logar_user')
def grammar_list(request):
    grammar = Grammar.objects.filter(criado_por=request.user)
    context = {
        'grammar': grammar,
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
            return redirect('grammar:grammar_list')
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
        return redirect('grammar:grammar_list')
    
    context = {
        "form_grammar":form_grammar
    }
    return render(request, 'grammar_form.html', context)

@login_required(login_url='user:logar_user')
def grammar_delete(request, pk):
    grammar = Grammar.objects.get(id = pk)
    grammar.delete()
    return redirect('grammar:grammar_list')


