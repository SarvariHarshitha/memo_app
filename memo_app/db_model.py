from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional
from datetime import datetime
import reflex as rx

# Define the model
class User(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
    created_at: Optional[datetime] = Field(default_factory=datetime.now)

class MemoText(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int
    created_at: Optional[datetime] = Field(default_factory=datetime.now)

class MemoAudio(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    audio: str
    user_id: int
    created_at: Optional[datetime] = Field(default_factory=datetime.now)

class MemoImage(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    user_id: int
    created_at: Optional[datetime] = Field(default_factory=datetime.now)