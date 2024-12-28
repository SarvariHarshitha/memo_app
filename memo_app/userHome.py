import reflex as rx
from memo_app.sidebar import navbar_buttons
from memo_app.Components.addformtext import add_form_text, TextModel



class UserHomeState(TextModel):
    @rx.event
    def show_form(self):
        """Toggle the visibility of the form."""
        self.can_show = not self.can_show

def user_home():
    return rx.box(
        navbar_buttons(),
        rx.heading("Text", size= "8", margin_top="2rem", margin_left="2rem"),
        rx.grid(
            rx.card(
                rx.button(
                    "+",
                    width="4rem",
                    height="2rem",
                    on_click=UserHomeState.show_form,  
                ),
                height="15rem",
                padding="4rem 40%",
            ),
            rx.foreach(TextModel.get_text_data,  
                       lambda data: rx.card(rx.scroll_area(rx.heading(data.title), rx.text(data.content), rx.button(rx.icon("delete"), on_click=TextModel.delete_text(data.id), margin_top="1rem")), height="15rem",)),
            columns="3",
            gap="5",
            spacing="5",
            width="100%",
            margin_top="2rem",
        ),
        rx.cond(UserHomeState.can_show, add_form_text()),  # Show the form when can_show is True
    )
