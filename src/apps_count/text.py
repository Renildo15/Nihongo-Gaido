from text_app.models import TextTraducao, TextWriting, Text

def get_text_translate(request):
    return TextTraducao.objects.filter(criado_por = request.user)

def get_text_writing(request):
    return TextWriting.objects.filter(criado_por = request.user)

def get_text(request):
    return Text.objects.filter(criado_por = request.user)