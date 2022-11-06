from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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
