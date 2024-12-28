import reflex as rx

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("linkedin", "/#"),
        spacing="3",
        justify="end",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.heading(
                            "Memo App",
                            size="7",
                            weight="bold",
                        ),
                        align_items="center",
                    ),
                    rx.text(
                        "© 2024 Sarvari Harshitha",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="4",
                    align_items=[
                        "center",
                        "center",
                        "start",
                    ],
                ),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    spacing="4",
                    align="center",
                    width="100%",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        width="100%",
        bg = rx.color("accent", 3),
        align="end",
        justify="end",
        margin_top="3em",
        padding="1em",
    )