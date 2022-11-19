from django.contrib import admin
from .models import Text, TextTraducao, TextWriting
# Register your models here.
admin.site.register(Text)
admin.site.register(TextTraducao)
admin.site.register(TextWriting)