from phrases_app.models import Grammar_Phrase

def get_phrase(request):
    return Grammar_Phrase.objects.filter(criado_por = request.user)