from django.shortcuts import render
from .forms import TextForm,TextTraducaoForm,TextWriting
# Create your views here.

def text_create(request):
    text_form = TextForm
    context = {
        "text_form":text_form
    }
    return render(request, 'text_form.html', context)
