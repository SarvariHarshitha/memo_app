import reflex as rx
from memo_app.darkmode import dark_mode_toggle
from memo_app.auth import AuthState 
from memo_app.base import State

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )

def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Memo App", size="7", weight="bold",
                        on_click=rx.redirect("/user"),
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    dark_mode_toggle(),
                    spacing="2",
                ),
                rx.hstack(
                    navbar_link("Text", "/user"),
                    navbar_link("Audio", "/user/audio"),
                    navbar_link("Image", "/user/image"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Profile",
                        size="3",
                        variant="outline",
                        on_click=rx.redirect("/user/profile"),
                    ),
                    rx.button("Logout", size="3",
                              on_click=State.logout
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
                        "Memo App", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Text", on_select=rx.redirect("/user")),
                        rx.menu.item("Audio", on_select=rx.redirect("/user/audio")),
                        rx.menu.item("Image", on_select=rx.redirect("/user/image")),
                        rx.menu.item("Profile", on_select=rx.redirect("/user/profile")),
                        rx.menu.item("Logout", on_select=State.logout),
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
