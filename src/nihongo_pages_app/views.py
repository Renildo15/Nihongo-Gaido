from django.shortcuts import render
from apps_count.grammar import get_grammar
from django.contrib.auth.decorators import login_required

@login_required(login_url='user:logar_user')
def home(request):
    grammar = get_grammar(request)

    context = {
        'grammar': grammar
    }
    return render(request, 'pages/index.html', context)

@login_required(login_url='user:logar_user')
def sobre(request):
    return render(request, 'pages/sobre.html')