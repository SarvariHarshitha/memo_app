import reflex as rx
from memo_app.base import State
from memo_app.db_model import MemoText
from sqlmodel import select



class TextModel(State):
    """Handles saving MemoText to the database."""

    title: str = ""
    content: str = ""
    can_show: bool = False
    

    def save(self):
        """Save the memo to the database."""
        if State.user is None:
            print("No user logged in.")
            return rx.redirect("/login")

        user_id = self.user.id
        print(f"User ID: {user_id}")
        with rx.session() as session:
            memo = MemoText(title=self.title, content=self.content, user_id=user_id)
            session.add(memo)
            session.commit()
            self.can_show = False
            print("Added")
            return rx.redirect("/user")
    
    @rx.var
    def get_text_data(self) -> list[MemoText]:
        if self.logged_in:
            with rx.session() as session:
                return session.exec(select(MemoText).where(MemoText.user_id == self.user.id)).all()
        return []
    
    @rx.event
    def delete_text(self, text_id):
        """Delete a text entry from the database."""
        with rx.session() as session:
            text_to_delete = session.get(MemoText, text_id)
            if text_to_delete:
                session.delete(text_to_delete)
                session.commit()
            