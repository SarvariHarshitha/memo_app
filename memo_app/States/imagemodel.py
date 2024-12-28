import reflex as rx
from memo_app.base import State
from memo_app.db_model import MemoImage
from sqlmodel import select
import base64

class ImageModel(State):
    """Handles saving MemoImage to the database."""

    title: str = ""
    imageBase64: str = ""  # Store Base64 encoded string of the image
    can_show: bool = False

    async def set_image(self, files: list[rx.UploadFile]):
        """Convert the uploaded image file (already in bytes) to Base64."""
        # Read the file as bytes and then encode it in Base64
        image_bytes = await files[0].read()
        self.imageBase64 = base64.b64encode(image_bytes).decode("utf-8")  # Convert bytes to Base64 string

    def save(self):
        """Save the memo to the database."""
        if State.user is None:
            print("No user logged in.")
            return rx.redirect("/login")

        user_id = self.user.id
        print(f"User ID: {user_id}")
        with rx.session() as session:
            # Save the Base64 encoded image in the database
            memo = MemoImage(title=self.title, image=self.imageBase64, user_id=user_id)
            session.add(memo)
            session.commit()
            self.can_show = False
            print("Added")
            return rx.redirect("/user/image")
    
    @rx.var
    def get_image_data(self) -> list[MemoImage]:
        """Fetch image data for the logged-in user."""
        if self.logged_in:
            with rx.session() as session:
                return session.exec(select(MemoImage).where(MemoImage.user_id == self.user.id)).all()
        return []
    
    @rx.event
    def delete_image(self, image_id):
        """Delete an image entry from the database."""
        with rx.session() as session:
            image_to_delete = session.get(MemoImage, image_id)
            if image_to_delete:
                session.delete(image_to_delete)
                session.commit()
