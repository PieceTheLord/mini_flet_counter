import flet as ft
from reqs.reqs  import Data

def main(page: ft.Page):
    page.title = "Counter app"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    txt_number = ft.TextField(
        value=Data.get_count(), text_align=ft.TextAlign.RIGHT, width=400
    )

    def minus_click(e):
        txt_number.value = Data.minus_one_count()
        page.update()

    def plus_click(e):
        txt_number.value = Data.add_one_count()
        page.update()

    page.add(
        ft.Container(
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ]
            ),
            alignment=ft.alignment.center,
            width=page.window.width,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
