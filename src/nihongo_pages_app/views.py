from django.shortcuts import render
from apps_count.grammar import get_grammar
from apps_count.example import get_example
from apps_count.phrase import get_phrase
from apps_count.text import get_text, get_text_translate, get_text_writing
from apps_count.vocabulary import get_word, get_category, get_conjugation
from django.contrib.auth.decorators import login_required

@login_required(login_url='user:logar_user')
def home(request):
    grammar = get_grammar(request)
    example = get_example(request)
    phrase = get_phrase(request)
    text = get_text(request)
    text_translate = get_text_translate(request)
    text_writing = get_text_writing(request)
    word = get_word(request)
    category = get_category(request)
    conjugation = get_conjugation(request)
    

    context = {
        'grammar': grammar,
        'example': example,
        'phrase': phrase,
        'text': text,
        'text_translate':text_translate,
        'text_writing' : text_writing,
        'word':word,
        'category': category,
        'conjugation': conjugation
    }
    return render(request, 'pages/index.html', context)

@login_required(login_url='user:logar_user')
def sobre(request):
    return render(request, 'pages/sobre.html')