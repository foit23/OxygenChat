import enum
import uuid

from sqlalchemy.orm import (
    Mapped, mapped_column
)
from sqlalchemy import (
    String, Integer, Boolean
)
from Base import Base


class ChatType(enum.Enum):
    SYSTEM = 0
    PRIVATE_USER = 1
    PRIVATE = 2
    PUBLIC = 3

class Chat(
    Base
):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    uuid: Mapped[str] = mapped_column(String(), nullable=False,
                                      default= lambda: uuid.uuid4())
    chatname: Mapped[str] = mapped_column(String(), nullable=False)
    chattype: Mapped[int] = mapped_column(Integer(), nullable=False,
                                          default=ChatType.PRIVATE)
    isPublic: Mapped[bool] = mapped_column(Boolean(), nullable=False,
                                           default=True)
    username: Mapped[str] = mapped_column(String(), nullable=True)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    avatar_path: Mapped[str] = mapped_column(String(), nullable=True)
    ownerid: Mapped[int] = mapped_column(Integer(), nullable=True)
    admins: Mapped[str] = mapped_column(String(), nullable=True) #JSON type
    members: Mapped[str] = mapped_column(String(), nullable=False)
    isCrypted: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=True)
