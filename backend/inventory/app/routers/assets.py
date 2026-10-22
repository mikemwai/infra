from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.asset import AssetCreate, AssetOut, Environment
from app.services import assets as asset_service

router = APIRouter(prefix="/assets", tags=["assets"])

@router.post("", response_model=AssetOut, status_code=201)
def create_asset(payload: AssetCreate, db: Session = Depends(get_db)):
    try:
        return asset_service.create_asset(db, payload)
    except asset_service.DuplicateAssetError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("", response_model=list[AssetOut])
def list_assets(environment: Environment | None = None, db: Session = Depends(get_db)):
    return asset_service.list_assets(db, environment)

@router.get("/{asset_id}", response_model=AssetOut)
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = asset_service.get_asset(db, asset_id)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset