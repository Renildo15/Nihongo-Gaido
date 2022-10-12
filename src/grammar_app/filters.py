from dataclasses import fields
import django_filters
from .models import *

class orderFilter(django_filters.Filteret):
    class Meta:
        model: Grammar
        fields = "nivel"