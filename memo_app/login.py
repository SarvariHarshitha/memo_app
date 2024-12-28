import reflex as rx
from memo_app.auth import AuthState


def login_default() -> rx.Component:
    return rx.center(rx.card(rx.form(
        rx.vstack(
            rx.center(
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Email address",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="user@reflex.dev",
                    type="email",
                    size="3",
                    width="100%",
                    name="email",
                    on_blur=AuthState.set_email
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                    name="password",
                    on_blur=AuthState.set_password
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%", type="submit"),
            rx.center(
                rx.text("New here?", size="3"),
                rx.link("Sign up", href="/signup", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
            ),
            spacing="6",
            width="100%",
        ),
        on_submit= AuthState.login,
        reset_on_submit=True
    ),
    size="4",
    max_width="28em",
    width="100%",
    justify="center",
    align_items="center"
    ), margin_top="5em")
