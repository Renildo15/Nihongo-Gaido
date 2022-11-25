from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import TextForm,TextTraducaoForm,TextWritingForm
from .models import Text,TextTraducao, TextWriting
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests , random
# Create your views here.


@login_required(login_url='user:logar_user')
def text_list(request):
    texts = Text.objects.filter(criado_por=request.user.id)
    text_contains_query = request.GET.get('text_contains')

    if text_contains_query != '' and text_contains_query is not None:
        texts = Text.objects.filter(criado_por=request.user.id, titulo__icontains = text_contains_query)

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
@login_required(login_url='user:logar_user')
def text_traducao_create(request, slug):
    text_texto = Text.objects.get(slug=slug)
    initial_dict = {
            "titulo_traducao" : text_texto 
    }
    if request.method == "POST":
        text_traducao_form = TextTraducaoForm(request.POST or None, initial= initial_dict)
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

@login_required(login_url='user:logar_user')
def text_traducao_view(request, slug):
    try:
        text_traducao = TextTraducao.objects.get(slug=slug)
    except TextTraducao.DoesNotExist:
        text_traducao = None
        
    context = {
        "text_traducao": text_traducao,
    }

    return render(request, "text_traducao/text_traducao_view.html", context)

@login_required(login_url='user:logar_user')
def text_traducao_update(request, slug):
    text_traducao = get_object_or_404(TextTraducao, slug=slug)
    text_traducao_form = TextTraducaoForm(request.POST or None, instance=text_traducao)
    text_texto = Text.objects.get(slug=slug)

    if  text_traducao_form.is_valid():
        text_traducao_form.save()
        return redirect("text:text_view", slug=slug)
    context = {
        'text_traducao_form':text_traducao_form,
         "text": text_texto
    }

    return render(request,"text_traducao/text_traducao_form.html", context)

@login_required(login_url='user:logar_user')
def text_traducao_delete(request, slug):
    text_traducao = TextTraducao.objects.get(slug=slug)
    text_traducao.delete()
    messages.success(request, "Texto deletado com sucesso!")
    return redirect(reverse('text:text_list'))


###############################Texto escrita############################################

def theme_choose(request):
    api = "https://api-temas.herokuapp.com/temas"

    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
          print("A resposta não chegou com o formato esperado.")

    dic = {}

    for i, value in enumerate(lista):
        dic[i] = value

    theme = random.choice(list(dic.values()))

    return theme['tema']




@login_required(login_url='user:logar_user')
def text_list_w(request):
    texts = TextWriting.objects.filter(criado_por=request.user.id)
    text_contains_query = request.GET.get("text_w_contains")

    if text_contains_query != '' and text_contains_query is not None:
        texts = TextWriting.objects.filter(criado_por=request.user.id, titulo__icontains=text_contains_query)
    context = {
        "texts":texts
    }

    return render(request, "text_escrita/text_list_w.html", context)


@login_required(login_url='user:logar_user')
def text_create_w(request):
    theme = theme_choose(request)
    if request.method == "POST":
        text_form = TextWritingForm(request.POST or None)

        if text_form.is_valid():
            text = text_form.save(commit=False)
            text.criado_por = request.user
            messages.success(request,"Texto salvo com sucesso!")
            text.save()
            return redirect(reverse("text:text_escrito_form"))
    else:
         
         text_form = TextWritingForm()

    context = {
        'text_form': text_form,
        'theme': theme
    }

    return render(request, "text_escrita/text_form_w.html", context)

@login_required(login_url='user:logar_user')
def text_view_w(request, slug):
    try:
        texts = TextWriting.objects.get(slug=slug)
    except TextWriting.DoesNotExist:
        texts = None

    context = {
        "texts": texts
    }

    return render(request,"text_escrita/text_view_w.html", context)

@login_required(login_url='user:logar_user')
def text_update_w(request, slug):
    text = get_object_or_404(TextWriting, slug=slug)
    text_form = TextWritingForm(request.POST or None, instance=text)

    if text_form.is_valid():
        text_form.save()
        messages.success(request, "Texto alterado com sucesso!")
        return redirect('text:text_escrito_view', slug=slug)

    context = {
        'text_form':text_form
    }

    return render(request, "text_escrita/text_edit_w.html", context)

@login_required(login_url='user:logar_user')
def text_delete_w(request, slug):
    text = TextWriting.objects.get(slug=slug)
    text.delete()
    messages.success(request, "Texto deletado com sucesso!")
    return redirect(reverse("text:text_escrito_list"))
