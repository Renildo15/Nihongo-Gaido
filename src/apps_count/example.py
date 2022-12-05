from example_app.models import Example

def get_example(request):
    return Example.objects.filter(criado_por = request.user)