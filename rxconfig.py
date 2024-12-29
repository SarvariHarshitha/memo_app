import reflex as rx
from dotenv import load_dotenv
import os
load_dotenv()


config = rx.Config(
    app_name="memo_app",
    db_url=os.getenv("DB_URL")
)