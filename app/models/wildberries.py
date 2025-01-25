from sqlalchemy import Integer, String, PrimaryKeyConstraint, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class WildberriesProductDB(Base):
    __tablename__ = 'wildberries_product'  # noqa
    __table_args__ = (
        PrimaryKeyConstraint('name'),
        Index('ix_article', 'article', unique=True),
    )

    name: Mapped[str] = mapped_column(String, nullable=False)
    article: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    sale_price: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    total_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
