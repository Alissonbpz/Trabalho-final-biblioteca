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

def livro(request, id):
    try:
        l = Livro.objects.get(id=id)
    except Livro.DoesNotExist:
        return JsonResponse({"erro": "Livro não encontrado"}, status=404)
    return JsonResponse(mdp_dicionario(l))

def lista_livros(request):
    livros = Livro.objects.all()
    busca = request.GET.get("busca")
    if busca:
        livros = livros.filter(titulo__icontains=busca)
    dados = []
    for livro in livros:
        dados.append(mdp_dicionario(livro))
    return JsonResponse({"livros": dados})