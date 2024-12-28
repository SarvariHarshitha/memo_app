import reflex as rx
from memo_app.sidebar import navbar_buttons
from memo_app.Components.addformimage import add_form_image, ImageModel
import base64

class ImageState(ImageModel):

    @rx.event
    def show_form(self):
        """Toggle the visibility of the form."""
        self.can_show = not self.can_show

def image():
    return rx.box(
        navbar_buttons(),
        rx.heading("Images", size= "8", margin_top="2rem", margin_left="2rem"),
        rx.grid(
            rx.card(
                rx.button(
                    rx.icon("plus"),
                    width="4rem",
                    height="2rem",
                    on_click=ImageState.show_form,
                ),
                height="15rem",
                padding="4rem 40%",
            ),
            rx.foreach(ImageModel.get_image_data,  
                       lambda data: rx.card(
                           rx.scroll_area(rx.heading(data.title),
                           rx.image(f"data:image/jpeg;base64,{data.image}"),  
                           rx.button(rx.icon("delete"), on_click=ImageModel.delete_image(data.id), margin_top="1rem")),
                            height="15rem",
                       )),
            columns="3",
            gap="5",
            spacing="5",
            width="100%",
            margin_top="2rem"
        ),
        rx.cond(ImageState.can_show, add_form_image())
    )
