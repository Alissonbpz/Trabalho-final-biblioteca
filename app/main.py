import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Biblioteca"
    
    lista = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    aviso = ft.Text("", size=12, color=ft.Colors.RED_600)

    def carregar(e=None):
        lista.controls.clear()
        try:
            resp = requests.get(URL)
        except requests.exceptions.ConnectionError:
            aviso.value = "Não foi possível conectar à API. Ela está ligada?"
            page.update()
            return
        livros = resp.json()["..."]
        for livro in livros:
            if livro["disponivel"]:
                status = "Disponível"
            else:
                status = ...
            lista.controls.append(
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Text(
                            f'{livro["titulo"]} - {livro["autor"]} ({livro["ano"]}) | {status}'
                        ),
                    )
                )
            )
        aviso.value = ""
        page.update()

    botao = ft.Button(content=ft.Text("Atualizar"), on_click=carregar)

    page.add(botao, lista, aviso)
    carregar()



ft.run(main)