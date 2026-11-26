# Trabalho-final-biblioteca
Projeto final da disciplina de Programação III: desenvolvimento de um sistema de biblioteca utilizando Django para criar uma API REST, com banco de dados SQLite, e Flet para desenvolver a interface gráfica. O sistema permite listar, pesquisar, cadastrar, editar e excluir livros, com validação dos dados e comunicação entre o aplicativo e a API.

## Integrantes

- Alisson Paz
- Eduardo Jacobi

## Estrutura do projeto

- `api/`: projeto Django (API REST), com o banco `db.sqlite3` e o `requirements.txt`
- `app/`: aplicativo usando Flet que consome a API

### API (Django)

Na pasta `api`, no terminal:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver
```

A API fica em `http://127.0.0.1:8000/livros/`

## Rotas da API

| Método | Rota | Sucesso | Erros possíveis |
|--------|------|---------|-----------------|
| GET | `/livros/` | 200 · a lista | — |
| GET | `/livros/?busca=python` | 200 · a lista filtrada | — |
| POST | `/livros/` | 201 · o livro criado | 400 |
| GET | `/livros/<id>/` | 200 · o livro | 404 |
| PUT | `/livros/<id>/` | 200 · o livro alterado | 400 · 404 |
| DELETE | `/livros/<id>/` | 204 · sem corpo | 404 |

### App (Flet)

Com a API ligada, abra outro terminal na raiz do projeto:

```
.venv\Scripts\Activate.ps1
python -m pip install -r app/requirements.txt
cd app
python main.py
```

A API precisa estar rodando antes de abrir o app. O app lista, busca, cadastra, edita e exclui livros, e mostra avisos quando o servidor está rodando ou a API devolve o erro.