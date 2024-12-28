import reflex as rx
from memo_app.sidebar import navbar_buttons
from memo_app.Components.addformaudio import add_form_audio, AudioModel  # New component for adding audio
import base64

class AudioState(AudioModel):

    @rx.event
    def show_form(self):
        """Toggle the visibility of the audio upload form."""
        self.can_show = not self.can_show

def audio():
    return rx.box(
        navbar_buttons(),
        rx.heading("Audios", size="8", margin_top="2rem", margin_left="2rem"),
        rx.grid(
            rx.card(
                rx.button(
                    rx.icon("plus"),
                    width="4rem",
                    height="2rem",
                    on_click=AudioState.show_form,  # Toggle the form visibility for uploading audio
                ),
                height="15rem",
                padding="4rem 40%",
            ),
            rx.foreach(AudioModel.get_audio_data,  
                       lambda data: rx.card(
                           rx.scroll_area(rx.heading(data.title),
                           rx.audio(
                               controls=True,  
                               url = f"data:audio/mp3;base64,{data.audio}" ,
                                width="100%",
                                    height="20%" 
                           ),
                           rx.button(rx.icon("delete"), on_click=AudioModel.delete_audio(data.id),margin_top="1rem")),
                        height="15rem",
                       )),
            columns="3",
            gap="5",
            spacing="5",
            width="100%",
            margin_top="2rem"
        ),
        rx.cond(AudioState.can_show, add_form_audio()) 
    )
