from django.shortcuts import render
from .models import Example
# Create your views here.

def example_list(request, slug):
    example = Example.objects.filter(criado_por=request.user.id, slug=slug)

    context = {
        "examples" : example
    }

    return render(request, "example_list.html", context)