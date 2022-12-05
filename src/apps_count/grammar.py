from grammar_app.models import Grammar

def get_grammar(request):
    return Grammar.objects.filter(criado_por = request.user)