import reflex as rx
from memo_app.darkmode import dark_mode_toggle

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Memo App", size="7", weight="bold",
                        on_click=rx.redirect("/"),
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    dark_mode_toggle(),
                    spacing="2",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                        on_click=rx.redirect("/signup"),
                    ),
                    rx.button("Log In", size="3",
                              on_click=rx.redirect("/login"),
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Memo App", size="6", weight="bold", on_click=rx.redirect("/")
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Log in", on_select=rx.redirect("/login")),
                        rx.menu.item("Sign up", on_select=rx.redirect("/signup")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%"
    )
