import reflex as rx
from memo_app.base import State
from memo_app.db_model import User
from sqlmodel import select

class UserModel(State):
    """Handles saving MemoText to the database."""

    old_password: str = ""
    new_password: str = ""
    confirm_password: str = ""

    @rx.event
    def change_password(self):
        """Change the password of the user."""
        if self.new_password != self.confirm_password:
            rx.window_alert("Passwords do not match.")
            return

        user_id = self.user.id
        with rx.session() as session:
            user = session.get(User, user_id)
            if user.password == self.old_password:
                print(f"User ID: {user_id}")
                user.password = self.new_password
                session.add(user)
                session.commit()
                rx.window_alert("Password changed")
                return rx.redirect("/user")
            else:
                rx.window_alert("Old password is incorrect.")
                return
    

    