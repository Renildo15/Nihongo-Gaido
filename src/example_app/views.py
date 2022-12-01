from django.shortcuts import render
from django.urls import reverse
from .models import Example
from vocabulary_app.models import Word
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExampleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='user:logar_user')
def example_list(request, slug):
    example_contains_query = request.GET.get("example_contains")
    word = Word.objects.get(slug=slug)

    if example_contains_query != '' and example_contains_query is not None:
        example = Example.objects.filter(criado_por=request.user.id, slug=slug, frase__icontains = example_contains_query)
    else:
         example = Example.objects.filter(criado_por=request.user.id, slug=slug)

    
    context = {
        "examples" : example,
        'word': word
    }

    return render(request, "example_list.html", context)

@login_required(login_url='user:logar_user')
def example_create(request,slug):
    word = Word.objects.get(slug=slug)
    initial_dict = {
            "leitura" : word.leitura
    }
    
    if request.method == "POST":
        form_example = ExampleForm(request.POST or None, initial=initial_dict)
        if form_example.is_valid():
            example = form_example.save(commit=False)
            example.palavra = word
            example.leitura = initial_dict['leitura']
            example.criado_por = request.user
            example.save()
            messages.success(request,"Exemplo adicionada com sucesso!")
            return redirect(reverse("vocabulary:word_list"))
    else:
        form_example = ExampleForm(initial=initial_dict)

    context = {
        "form_example": form_example,
       
    }

    return render(request,'example_form.html', context)


@login_required(login_url='user:logar_user')
def example_edit(request, pk):
    example = get_object_or_404(Example, pk=pk)
    form_example = ExampleForm(request.POST or None, instance=example)

    if form_example.is_valid():
        form_example.save()
        messages.success(request, "Exemplo alterado com sucesso!")
        return redirect("example:example_list", pk=pk)


    context = {
        "form_example" : form_example
    }

    return render(request, "example_edit.html", context)


@login_required(login_url='user:logar_user')
def example_delete(request, pk):
    example = Example.objects.get(pk=pk)
    example.delete()
    messages.success(request, "Exemplo deletado com sucesso!")
    return redirect(reverse("vocabulary:word_list"))