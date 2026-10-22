from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate

class DuplicateAssetError(Exception):
    pass

def create_asset(db: Session, payload: AssetCreate) -> Asset:
    asset = Asset(**payload.model_dump())
    db.add(asset)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise DuplicateAssetError(
            f"{payload.name} already exists in {payload.environment}"
        )
    db.refresh(asset)
    return asset

def list_assets(db: Session, environment: str | None = None) -> list[Asset]:
    stmt = select(Asset).order_by(Asset.id)
    if environment:
        stmt = stmt.where(Asset.environment == environment)
    return list(db.scalars(stmt))


def get_asset(db: Session, asset_id: int) -> Asset | None:
    return db.get(Asset, asset_id)