from vocabulary_app.models import Category, Word, Conjugation

def get_category(request):
    return Category.objects.filter(criado_por = request.user)

def get_word(request):
    return  Word.objects.filter(criado_por = request.user)

def get_conjugation(request):
    return Conjugation.objects.filter(criado_por = request.user)