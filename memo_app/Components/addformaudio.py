import reflex as rx
from memo_app.States.audiomodel import AudioModel

def add_form_audio():
    return rx.box(
        rx.form(
            rx.input(
                placeholder="Title",
                margin_bottom="1rem",
                on_change=AudioModel.set_title  # Bind to the title input field
            ),
            rx.upload(
                rx.vstack(
                    rx.text(
                        "Drag and drop files here or click to select audio files"
                    ),
                ),
                label="Upload Audio",
                margin_bottom="1rem",
                id="audio",
                accept={
                    "audio/mp3": [".mp3"],
                    "audio/wav": [".wav"],
                    "audio/mpeg": [".mp3"],
                    # Add other audio formats as needed
                },
                on_drop=AudioModel.set_audio(rx.upload_files("audio")),  # Handle audio file upload
            ),
            rx.button(
                "Add",
                width="100%",
                margin_bottom="1rem",
                type="submit",
                on_click=AudioModel.save  # Save the audio to the database
            ),
        ),
        padding="2rem",
        width="40%",
        bg=rx.color("accent", 3),
        style={
            "position": "absolute",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",  # Center the form
        },
    )
