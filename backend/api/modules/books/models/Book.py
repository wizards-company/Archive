from sqlalchemy import ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.schema import PrimaryKeyConstraint
import uuid

from api.shared.database.connection import Base

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True, name="books_id")
    userId: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.users_id'), nullable=False, name="users_id")    
    title: Mapped[str] = mapped_column(String(100), nullable=False, name="books_title")
    author: Mapped[str] = mapped_column(String(100), nullable=False, name="books_author")
    publisher: Mapped[str] = mapped_column(String(100), nullable=True, name="books_publisher")
    page: Mapped[int] = mapped_column(Integer(), nullable=True, name="books_qtd_page")
    datePublished: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True, name="books_dat_published")
    dateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False, default=func.now(), name="books_dat_created")

    user = relationship("User", back_populates="books")
