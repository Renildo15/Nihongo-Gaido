from django.shortcuts import render
from .forms import TextForm,TextTraducaoForm,TextWriting
from .models import Text,TextTraducao, TextWriting
# Create your views here.


def text_list(request):
    texts = Text.objects.filter(criado_por=request.user.id)
    context = {
        "texts": texts
    }
    return render(request, 'text_list.html', context)


def text_create(request):
    text_form = TextForm
    context = {
        "text_form":text_form
    }
    return render(request, 'text_form.html', context)
