from datetime import datetime

from sqlalchemy import DateTime, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class Asset(Base):
    __tablename__ = "assets"
    __table_args__ = (
        UniqueConstraint("name", "environment", name="uq_assets_name_environment"),
        {"schema": "inventory"},
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    environment: Mapped[str] = mapped_column(String(20), default="dev")
    owner_team: Mapped[str | None] = mapped_column(String(100))
    health_url: Mapped[str | None] = mapped_column(String(300))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )