from typing import Optional
from pydantic import BaseModel, Field
from .base import CoreModel

class LocationBase(CoreModel):
    name: str
    address: Optional[str] = None
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class LocationCreate(LocationBase):
    pass

class LocationUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)

class LocationRead(LocationBase):
    id: int

    class Config:
        from_attributes = True
