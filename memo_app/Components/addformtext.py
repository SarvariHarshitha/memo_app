import reflex as rx
from memo_app.States.textmodel import TextModel

def add_form_text():
    return rx.box(
        rx.form(
            rx.input(
                placeholder="Title",
                margin_bottom="1rem",
                on_change=TextModel.set_title
            ),
            rx.text_area(
                placeholder="Content",
                height="10rem",
                margin_bottom="1rem",
                on_change=TextModel.set_content
            ),
            rx.button(
                "Add",
                width="100%",
                margin_bottom="1rem",
                type="submit",
                on_click=TextModel.save  
            ),
        ),
        padding="2rem",
        width="40%",
        bg=rx.color("accent", 3),
        position="absolute",
        top="30%",
        left="20%",
    )
