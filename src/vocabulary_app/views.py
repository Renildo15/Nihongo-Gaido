from django.shortcuts import render
from .models import *
# Create your views here.
def word_list(request):
    word = Word.objects.filter(criado_por=request.user.id)

    context = {
        "words": word
    }

    return render(request, "word_list.html", context)