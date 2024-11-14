from returns.maybe import Maybe

from app.db.postgresql.models import Location
from app.db.postgresql.postgresql_database import session_maker


def find_location_by_location_id(location_id: int) -> Maybe[Location]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(Location)
                                   .filter(Location.location_id == location_id)
                                   .first())

def find_location_by_terrorist_id(terrorist_id: str) -> Maybe[Location]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Location)
                                   .filter(Location.terrorist_id == terrorist_id)
                                   .first())

def create_new_location(new_location: Location) -> Location:
    with session_maker() as session:
        session.add(new_location)
        session.commit()
        session.refresh(new_location)
        return new_location
