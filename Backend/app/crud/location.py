from typing import Any, Union
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2.elements import WKTElement
from app.crud.base import CRUDBase
from app.models.location import Location
from app.schemas.location import LocationCreate, LocationUpdate

class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    async def create(self, db: AsyncSession, *, obj_in: LocationCreate) -> Location:
        obj_in_data = obj_in.model_dump(exclude={"latitude", "longitude"})
        # Create POINT(longitude latitude) - Note the order!
        point = f"POINT({obj_in.longitude} {obj_in.latitude})"
        db_obj = self.model(
            **obj_in_data,
            point=WKTElement(point, srid=4326)
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db: AsyncSession,
        *,
        db_obj: Location,
        obj_in: Union[LocationUpdate, dict[str, Any]]
    ) -> Location:
        update_data: dict[str, Any]
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        
        if "latitude" in update_data or "longitude" in update_data:
            lat = update_data.get("latitude", 0) 
            lon = update_data.get("longitude", 0)
            point = f"POINT({lon} {lat})"
            update_data["point"] = WKTElement(point, srid=4326)
            update_data.pop("latitude", None)
            update_data.pop("longitude", None)

        return await CRUDBase.update(self, db, db_obj=db_obj, obj_in=update_data)

location = CRUDLocation(Location)
