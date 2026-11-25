import flet as ft
import requests

URL = "http://127.0.0.1:8000/livros/"

def main(page: ft.Page):
    page.title = "Biblioteca"
    
    lista = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    aviso = ft.Text("", size=12, color=ft.Colors.RED_600)
    busca_livro = ft.TextField(label="Buscar por título", width=320)

    def abrir_formulario():
            titulo = ft.TextField(label="Título")
            autor = ft.TextField(label="Autor")
            ano = ft.TextField(label="Ano")
            disponivel = ft.Checkbox(label="Disponível", value=True)
            txt_erro = ft.Text("", color = ft.Colors.RED_600)


            def cancelar(e):
                page.pop_dialog()


            def salvar(e):
                dados = {
                    "titulo": titulo.value,
                    "autor": autor.value,
                    "ano": ano.value,
                    "disponivel": disponivel.value,
                }
                try:
                    resp = requests.post(URL, json=dados)
                except requests.exceptions.ConnectionError:
                    txt_erro.value = "Não foi possível conectar à API. O servidor está ligado?"
                    page.update()
                    return
                if resp.status_code == 400:
                    txt_erro.value = resp.json()["erro"]
                    page.update()
                    return
                page.pop_dialog()
                carregar()


            dialogo = ft.AlertDialog(
                title=ft.Text("Novo livro"),
                content=ft.Column([titulo, autor, ano, disponivel, txt_erro], tight=True),
                actions=[
                    ft.TextButton("Cancelar", on_click=cancelar),
                    ft.TextButton("Salvar", on_click=salvar),
                ],
            )
            page.show_dialog(dialogo)

    def excluir(livro_id):
        try:
            resp = requests.delete(f"{URL}{livro_id}/")
        except requests.exceptions.ConnectionError:
            aviso.value = "Não foi possível conectar à API. Ela está ligada?"
            page.update()
            return
        carregar()
        if resp.status_code == 404:
            aviso.value = "Esse livro não existe mais."
            page.update()

    def confirmar_exclusao(livro):
        def sim(e):
            page.pop_dialog()
            excluir(livro["id"])

        def nao(e):
            page.pop_dialog()

        dialogo = ft.AlertDialog(
            title=ft.Text("Excluir livro"),
            content=ft.Text(f'Deseja excluir "{livro["titulo"]}"?'),
            actions=[
                ft.TextButton("Não", on_click=nao),
                ft.TextButton("Sim", on_click=sim),
            ],
        )
        page.show_dialog(dialogo)

    def carregar(e=None):
        lista.controls.clear()
        try:
            resp = requests.get(URL, params={"busca": busca_livro.value})
        except requests.exceptions.ConnectionError:
            aviso.value = "Não foi possível conectar à API. Ela está ligada?"
            page.update()
            return
        livros = resp.json()["livros"]
        for livro in livros:
            if livro["disponivel"]:
                status = "Disponível"
            else:
                status = "Indisponível"
            lista.controls.append(
               ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    f'{livro["titulo"]} - {livro["autor"]} ({livro["ano"]}) | {status}',
                                    expand=True,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    on_click=lambda e, l=livro: confirmar_exclusao(l),
                                ),
                            ]
                        ),
                    )
                )
            )
        aviso.value = ""
        page.update()

    botao = ft.Button(content=ft.Text("Atualizar"), on_click=carregar)
    botao_cadastrar_livro = ft.Button(content=ft.Text("Cadastrar livro"), on_click=lambda e: abrir_formulario())

    page.add(busca_livro, botao, botao_cadastrar_livro, lista, aviso)
    carregar()

ft.run(main)