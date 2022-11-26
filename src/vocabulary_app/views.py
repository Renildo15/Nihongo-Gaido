from django.shortcuts import render
from .models import *
# Create your views here.
def word_list(request):
    word = Word.objects.filter(criado_por=request.user.id)

    context = {
        "words": word
    }

    return render(request, "word_list.html", context)

def conjugation_list(request, slug):
    try:
        conjugations = Conjugation.objects.get(criado_por=request.user.id,slug=slug)
    except Conjugation.DoesNotExist:
        conjugations = None

    context = {
        "conjugations" : conjugations
    }

    return render(request, "conjugation_list.html", context)