from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    title: Mapped[str] = mapped_column(nullable=False)
    completed: Mapped[bool] = mapped_column(default=False)
    order: Mapped[int] = mapped_column(autoincrement=True, init=False, nullable=True)
