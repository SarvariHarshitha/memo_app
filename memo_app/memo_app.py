import reflex as rx

from memo_app.navbar import navbar_buttons
from memo_app.signup import signup_default
from memo_app.login import login_default
from memo_app.topbanner import top_banner_newsletter
from memo_app.home_section import home_section
from memo_app.footer import footer
from memo_app.userHome import user_home
from memo_app.base import State
from memo_app.audio import audio
from memo_app.image import image
from memo_app.user import user


from rxconfig import config



def index() -> rx.Component:
    return(
        navbar_buttons(),
        top_banner_newsletter(),
        home_section(),
        footer()
    )

def signup() -> rx.Component:
    return(
        navbar_buttons(),
        signup_default(),
        footer()
    )

def login() -> rx.Component:
    return(
        navbar_buttons(),
        login_default(),
        footer()
    )


app = rx.App()
app.add_page(index)
app.add_page(signup, "/signup")
app.add_page(login, "/login")
app.add_page(user_home, "/user", on_load=State.check_login)
app.add_page(audio, "/user/audio", on_load=State.check_login)
app.add_page(image, "/user/image", on_load=State.check_login)
app.add_page(user, "/user/profile", on_load=State.check_login)
