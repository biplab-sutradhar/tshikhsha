"""
Database model for the `users` table.
"""

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import VARCHAR

from .base import Base


class Users(Base):
    """
    Class is used to define the schema for storing user-related information.
    """

    username: Mapped[str] = mapped_column(
        VARCHAR(50), primary_key=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(VARCHAR(100), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)
