from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict

Environment = Literal["dev", "uat", "oat", "prod"]

class AssetCreate(BaseModel):
    name: str
    environment: Environment = "dev"
    owner_team: str | None = None
    health_url: str | None = None

class AssetOut(AssetCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime