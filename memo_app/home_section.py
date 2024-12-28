import reflex as rx

def home_section() -> rx.Component :
    return rx.center(
        rx.vstack(
        rx.heading(
            'Welcome to Memo App',
            size='8',
            as_='h2',
            align='center',
            spacing='3',
            width='100%',
            margin_top='2em',
            text_shadow='1px 1px 1px #fff'
        ),
        rx.text(
            'We help you to keep your thoughts organized.',
            size='4',
            spacing='3',
            width='100%',
            color_scheme='gray',
            margin_top='2em',
            align='center',
            justify='center',
        ),
        rx.grid(
            rx.card(
                rx.vstack(
                    rx.heading('Text'),
                    rx.text('Users can add text memos to the app.'),
                    rx.button('Learn More')
                ),
                bg= rx.color('accent',3)
            ),
            rx.card(
                rx.vstack(
                    rx.heading('Audio'),
                    rx.text('Users can add audio memos to the app.'),
                    rx.button('Learn More')
                ),
                bg= rx.color('accent',3),
            ),
            rx.card(
                rx.vstack(
                    rx.heading('Images'),
                    rx.text('Users can add image memos to the app.'),
                    rx.button('Learn More')
                ),
                bg= rx.color('accent',3),
            ),
            columns='3',
            gap = '1em',
            margin_top='2em',
         )
        )
    )