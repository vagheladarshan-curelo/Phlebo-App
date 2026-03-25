from sqlalchemy import Column, Integer, String, DateTime, func
from geoalchemy2 import Geometry
from app.core.database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    coords = Column(Geometry(geometry_type='POINT', srid=4326))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
