from django.shortcuts import render
from django.urls import reverse
from .models import Example
from vocabulary_app.models import Word
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExampleForm
from django.contrib import messages
# Create your views here.

def example_list(request, slug):
    example = Example.objects.filter(criado_por=request.user.id, slug=slug)
    word = Word.objects.get(slug=slug)
    context = {
        "examples" : example,
        'word': word
    }

    return render(request, "example_list.html", context)

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
            example.criado_por = request.user
            example.save()
            messages.success(request,"Palavra adicionada com sucesso!")
            return redirect(reverse('example:add_example'))
    else:
        form_example = ExampleForm(initial=initial_dict)

    context = {
        "form_example": form_example,
       
    }

    return render(request,'example_form.html', context)