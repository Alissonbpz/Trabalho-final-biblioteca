# Trabalho-final-biblioteca
Projeto final da disciplina de Programação III: desenvolvimento de um sistema de biblioteca utilizando Django para criar uma API REST, com banco de dados SQLite, e Flet para desenvolver a interface gráfica. O sistema permite listar, pesquisar, cadastrar, editar e excluir livros, com validação dos dados e comunicação entre o aplicativo e a API.

## Integrantes

- Alisson Paz
- Eduardo Jacobi

## Rotas da API

| Método | Rota | Sucesso | Erros possíveis |
|--------|------|---------|-----------------|
| GET | /livros/ | 200 · a lista | — |
| GET | /livros/?busca=python | 200 · a lista filtrada | — |
| POST | /livros/ | 201 · o livro criado | 400 |
| GET | /livros/<id>/ | 200 · o livro | 404 |
| PUT | /livros/<id>/ | 200 · o livro alterado | 400 · 404 |
| DELETE | /livros/<id>/ | 204 · sem corpo | 404 |