from django.http import JsonResponse
from .models import Livro

def mdp_dicionario(livro):
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano": livro.ano,
        "disponivel": livro.disponivel,
    }

def lista_livros(request):
    dados = []
    for livro in Livro.objects.all():
        dados.append(mdp_dicionario(livro))
    return JsonResponse({"livros": dados})
