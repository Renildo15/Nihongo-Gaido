from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def pagination(parametro_limit, grammar, parametro_page):
    if not parametro_limit.isdigit() or int(parametro_limit) <= 0:
        parametro_limit = '15'

    grammar_paginator = Paginator(grammar, parametro_limit)

    try:
        page = grammar_paginator.page(parametro_page)
    except (EmptyPage, PageNotAnInteger):
        page = grammar_paginator.page(1)

    return page

def verify_contains(grammar_contains_query, estrutura_contains_query, nivel_query, grammar):
    if grammar_contains_query:
        grammar = grammar.filter(gramatica__icontains=grammar_contains_query)
    elif estrutura_contains_query:
        grammar = grammar.filter(estrutura__icontains=estrutura_contains_query)
    elif nivel_query:
        grammar = grammar.filter(nivel__icontains=nivel_query)
    return grammar