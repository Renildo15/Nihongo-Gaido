from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import TextForm,TextTraducaoForm,TextWriting
from .models import Text,TextTraducao, TextWriting
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='user:logar_user')
def text_options(request):
    return render(request, "text_options.html")



@login_required(login_url='user:logar_user')
def text_list(request):
    texts = Text.objects.filter(criado_por=request.user.id)
    context = {
        "texts": texts
    }
    return render(request, 'text_list.html', context)



@login_required(login_url='user:logar_user')
def text_create(request):
    if request.method == "POST":
         text_form = TextForm(request.POST or None)
         
         if text_form.is_valid():
            text = text_form.save(commit=False)
            text.criado_por = request.user
            text.save()
            messages.success(request,"Texto adicionado com sucesso!")
            return redirect(reverse('text:add_text'))
    else:
        text_form = TextForm()
    context = {
        "text_form":text_form
    }
    return render(request, 'text_form.html', context)


@login_required(login_url='user:logar_user')
def text_view(request, slug):
    text = Text.objects.get(slug=slug)
    context = {
        "text":text
    }

    return render(request,"text_view.html", context)

@login_required(login_url='user:logar_user')
def text_update(request, slug):
    text = get_object_or_404(Text, slug=slug)
    print(text)
    text_form = TextForm(request.POST or None, instance=text)

    if text_form.is_valid():
        text_form.save()
        return redirect('text:text_list')
    context = {
        "text_form":text_form
    }

    return render(request, "text_form.html", context)

@login_required(login_url='user:logar_user')
def text_delete(request, slug):
    text = Text.objects.get(slug=slug)
    text.delete()
    messages.success(request, "Texto deletado com sucesso!")
    return redirect(reverse('text:text_list'))

################text tradução###############

def text_traducao_create(request, slug):
    text_texto = Text.objects.get(slug=slug)
    initial_dict = {
            "titulo_traducao" : text_texto 
    }
    print(request.user)
    if request.method == "POST":
        text_traducao_form = TextTraducaoForm(request.POST or None, initial= initial_dict)
        print( text_traducao_form)

        if text_traducao_form.is_valid():
            text = text_traducao_form.save(commit=False)
            text.criado_por = request.user
            text.text_id = text_texto
            text.save()
            messages.success(request,"Texto traduzido com sucesso!")
            return redirect(reverse("text:text_list"))
    else:
        text_traducao_form = TextTraducaoForm(initial= initial_dict)

    context = {
        "text_traducao_form":text_traducao_form,
        "text": text_texto
    }

    return render(request, "text_traducao/text_traducao_form.html", context)


def text_traducao_view(request, slug):
    try:
        text_traducao = TextTraducao.objects.get(slug=slug)
    except TextTraducao.DoesNotExist:
        text_traducao = None
        
    context = {
        "text_traducao": text_traducao
    }

    return render(request, "text_traducao/text_traducao_view.html", context)


def text_traducao_update(request, slug):
    text_traducao = get_object_or_404(TextTraducao, slug=slug)
    text_traducao_form = TextTraducaoForm(request.POST or None, instance=text_traducao)

    if  text_traducao_form.is_valid():
        text_traducao_form.save()
        return redirect("text:text_view", slug=slug)
    context = {
        'text_traducao_form':text_traducao_form
    }

    return render(request,"text_traducao/text_traducao_form.html", context)

def text_traducao_delete(request, slug):
    text_traducao = TextTraducao.objects.get(slug=slug)
    text_traducao.delete()
    messages.success(request, "Texto deletado com sucesso!")
    return redirect(reverse('text:text_list'))