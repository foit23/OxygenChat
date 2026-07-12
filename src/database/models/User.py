import uuid

from sqlalchemy.orm import (
    Mapped, mapped_column
)
from sqlalchemy import (
    String, Integer
)
from Base import Base


class User(
    Base
):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    uuid: Mapped[str] = mapped_column(String(), nullable=False,
                                      default=lambda: uuid.uuid4())
    phone: Mapped[int] = mapped_column(Integer(), nullable=True) #TODO: заглушка
    email: Mapped[str] = mapped_column(String(), nullable=True) #TODO: Заглушка
    username: Mapped[str] = mapped_column(String(), nullable=True)
    firstname: Mapped[str] = mapped_column(String(), nullable=False)
    lastname: Mapped[str] = mapped_column(String(), nullable=True)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    avatar_path: Mapped[str] = mapped_column(String(), nullable=True)
