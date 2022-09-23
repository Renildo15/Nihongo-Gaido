from django.contrib import admin
from grammar_app.models import Grammar
# Register your models here.

class GrammarAdmin(admin.ModelAdmin):
    readonly_fields = ('criado_por', )

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.criado_por = usuario
        super(GrammarAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(GrammarAdmin, self).get_queryset(request)
        qs = qs.filter(criado_por=request.user)
        return qs

admin.site.register(Grammar, GrammarAdmin)
