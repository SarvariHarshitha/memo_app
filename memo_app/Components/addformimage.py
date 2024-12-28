import reflex as rx
from memo_app.States.imagemodel import ImageModel

def add_form_image():
    return rx.box(
        rx.form(
            rx.input(
                placeholder="Title",
                margin_bottom="1rem",
                on_change=ImageModel.set_title 
            ),
            rx.upload(
                rx.vstack(
                    rx.text(
                        "Drag and drop files here or click to select files"
                    ),
                ),
                label="Upload image",
                margin_bottom="1rem",
                id="image",
                accept={
                "image/png": [".png"],
                "image/jpeg": [".jpg", ".jpeg"],
                },
                on_drop=ImageModel.set_image(rx.upload_files("image")),
            ),
            rx.button(
                "Add",
                width="100%",
                margin_bottom="1rem",
                type="submit",
                on_click=ImageModel.save  # Save the image to the database
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
