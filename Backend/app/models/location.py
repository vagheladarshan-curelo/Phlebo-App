from sqlalchemy import Column, String, Float
from geoalchemy2 import Geometry
from app.core.database import Base

class Location(Base):
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=True)
    # Using Geometry('POINT', srid=4326) for longitude/latitude
    point = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    
    def __repr__(self) -> str:
        return f"<Location(name={self.name}, address={self.address})>"
