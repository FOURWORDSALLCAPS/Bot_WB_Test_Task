from datetime import datetime

from sqlalchemy import BIGINT, TIMESTAMP, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        int: BIGINT,
        str: String(),
        datetime: TIMESTAMP(timezone=False),
    }

    create_date: Mapped[datetime] = mapped_column(server_default=func.now())
    update_date: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
