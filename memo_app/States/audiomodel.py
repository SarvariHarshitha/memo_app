import reflex as rx
from memo_app.base import State
from memo_app.db_model import MemoAudio
from sqlmodel import select
import base64

class AudioModel(State):
    """Handles saving MemoAudio to the database."""

    title: str = ""
    audioBase64: str = ""  # Store Base64 encoded string of the audio
    can_show: bool = False

    async def set_audio(self, files: list[rx.UploadFile]):
        """Convert the uploaded audio file (already in bytes) to Base64."""
        # Read the file as bytes and then encode it in Base64
        audio_bytes = await files[0].read()
        self.audioBase64 = base64.b64encode(audio_bytes).decode("utf-8")  # Convert bytes to Base64 string

    def save(self):
        """Save the memo to the database."""
        if State.user is None:
            print("No user logged in.")
            return rx.redirect("/login")

        user_id = self.user.id
        print(f"User ID: {user_id}")
        with rx.session() as session:
            # Save the Base64 encoded audio in the database
            memo = MemoAudio(title=self.title, audio=self.audioBase64, user_id=user_id)
            session.add(memo)
            session.commit()
            self.can_show = False
            print("Added")
            return rx.redirect("/user/audio")
    
    @rx.var
    def get_audio_data(self) -> list[MemoAudio]:
        """Fetch audio data for the logged-in user."""
        if self.logged_in:
            with rx.session() as session:
                return session.exec(select(MemoAudio).where(MemoAudio.user_id == self.user.id)).all()
        return []
    
    @rx.event
    def delete_audio(self, audio_id):
        """Delete an audio entry from the database."""
        with rx.session() as session:
            audio_to_delete = session.get(MemoAudio, audio_id)
            if audio_to_delete:
                session.delete(audio_to_delete)
                session.commit()
