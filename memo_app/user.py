import reflex as rx
from memo_app.sidebar import navbar_buttons
from memo_app.States.usermodel import UserModel, State

def user() -> rx.Component:
    return rx.box(
        navbar_buttons(),
        rx.heading("User", size="8", margin_top="2rem", margin_left="2rem"),
        
        rx.box(
            rx.text(f"User Email: {State.user.email}", size="5", margin_top="2rem", margin_left="2rem", font_weight="bold"),
        ),

        rx.center(rx.form(
            rx.vstack(
                # Old password input
                rx.input(
                    placeholder="Enter your old password",
                    type="password",
                    on_blur=UserModel.set_old_password,
                    width="100%",
                    border_radius="8px",
                    margin_bottom="1rem"
                ),

                # New password input
                rx.input(
                    placeholder="Enter your new password",
                    type="password",
                    on_blur=UserModel.set_new_password,
                    width="100%",
                    border_radius="8px",
                    margin_bottom="1rem"
                ),

                # Confirm password input
                rx.input(
                    placeholder="Confirm your new password",
                    type="password",
                    on_blur=UserModel.set_confirm_password,
                    width="100%",
                    border_radius="8px",
                    margin_bottom="2rem"
                ),

                rx.button(
                    "Change Password",
                    on_click=UserModel.change_password,
                    bg="blue.500",
                    color="white",
                    padding="1rem 2rem",
                    border_radius="8px",
                    _hover={"bg": "blue"},
                    font_weight="bold"
                ),
            ),
            bg=rx.color("accent", 3),
            padding="2rem",
            margin_top="2rem",
            width="40%",
            border_radius="10px",
            box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
            justify="center",
            align="center"
        )
        )
    )
