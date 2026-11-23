from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Livro
import json

def mdp_dicionario(livro):
    return {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "ano": livro.ano,
        "disponivel": livro.disponivel,
    }

def ler_json(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

@csrf_exempt
def lista_livros(request):
    if request.method == "POST":
        return cadastrar(request)
    livros = Livro.objects.all()
    busca = request.GET.get("busca")
    if busca:
        livros = livros.filter(titulo__icontains=busca)
    dados = []
    for l in livros:
        dados.append(mdp_dicionario(l))
    return JsonResponse({"livros": dados})

@csrf_exempt
def livro(request, id):
    try:
        a = Livro.objects.get(id=id)
    except Livro.DoesNotExist:
        return JsonResponse({"erro": "Livro não encontrado"}, status=404)
    if request.method == "PUT":
        return alterar(request, a)
    if request.method == "DELETE":
        a.delete()
        return HttpResponse(status=204)
    return JsonResponse(mdp_dicionario(a))

def validar(dados):
    if not dados.get("titulo"):
        return "O título é obrigatório"
    if not dados.get("autor"):
        return "O autor é obrigatório"
    try:
        ano = int(dados.get("ano"))
    except (TypeError, ValueError):
        return "O ano deve ser um número inteiro"
    if ano <= 0:
        return "O ano deve ser um número maior que zero"
    dados["ano"] = ano
    disponivel = dados.get("disponivel", True)
    if disponivel not in (True, False):
        return "O status de disponibilidade deve ser true ou false"
    return None

def cadastrar(request):
    dados = ler_json(request)
    if dados is None:
        return JsonResponse({"erro": "JSON inválido"}, status=400)
    erro = validar(dados)
    if erro:
        return JsonResponse({"erro": erro}, status=400)
    x = Livro.objects.create(
        titulo=dados["titulo"],
        autor= dados["autor"],
        ano=dados["ano"],
        disponivel=dados.get("disponivel", True),
    )
    return JsonResponse(mdp_dicionario(x), status=201)

def alterar(request, alt):
    dados = ler_json(request)
    if dados is None:
        return JsonResponse({"erro": "JSON inválido"}, status=400)
    erro = validar(dados)
    if erro:
        return JsonResponse({"erro": erro}, status=400)
    alt.titulo = dados["titulo"]
    alt.autor = dados["autor"]
    alt.ano = dados["ano"]
    alt.disponivel = dados.get("disponivel", True)
    alt.save()
    return JsonResponse(mdp_dicionario(alt), status=200)