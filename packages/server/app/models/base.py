"""
This base model provides common columns and configurations
for all models. It automatically generates the table name
(__table__) based on the class name.

Examples:
    Class Projects converts to "projects" in database
    Class UserProjectMapping converts to "user_project_mapping" in database
"""

import re
from datetime import datetime, timezone
from typing import Any

from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import BOOLEAN, TIMESTAMP


class Base(DeclarativeBase):
    """
    Declarative base class with common table field.
    """

    @declared_attr.directive
    def __tablename__(cls: Any) -> str:
        """
        Generate table name from class name. Converts camel case to snake_case.
        """
        table_name = re.sub("(?<!^)(?=[A-Z])", "_", cls.__name__).lower()
        return table_name

    is_active: Mapped[bool] = mapped_column(BOOLEAN, default=True, nullable=False)
    is_deleted: Mapped[bool] = mapped_column(BOOLEAN, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, default=datetime.now(timezone.utc), nullable=False
    )
    created_by: Mapped[str] = mapped_column(TEXT, default="system", nullable=False)
    updated_by: Mapped[str] = mapped_column(TEXT, default="system", nullable=False)
