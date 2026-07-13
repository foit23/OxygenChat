import enum
import uuid

from sqlalchemy.orm import (
    Mapped, mapped_column
)
from sqlalchemy import (
    String, Integer, Boolean
)
from Base import Base

class SenderType(enum.Enum):
    SYSTEM = 0
    USER = 1

class MessageType(enum.Enum):
    TEXT = 0
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    GIF = 4

class MessageForm(enum.Enum):
    CLASSIC = 0
    FORWARDED = 1
    COPIED = 2

class Message(
    Base
):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    uuid: Mapped[str] = mapped_column(String(), nullable=False,
                                      default=lambda: uuid.uuid4())
    text: Mapped[str] = mapped_column(String(), nullable=False)
    senderType: Mapped[int] = mapped_column(Integer(), nullable=False,
                                             default=SenderType.USER)
    messageType: Mapped[int] = mapped_column(Integer(), nullable=False)
    messageForm: Mapped[int] = mapped_column(Integer(), nullable=False,
                                             default=MessageForm.CLASSIC)
    view: Mapped[str] = mapped_column(String(), nullable=False) # JSON
    reactions: Mapped[str] = mapped_column(String, nullable=False) # JSON
    metaInfo: Mapped[str] = mapped_column(String(), nullable=False) # JSON
