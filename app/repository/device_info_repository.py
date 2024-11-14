from returns.maybe import Maybe

from app.db.postgresql.models import DeviceInfo
from app.db.postgresql.postgresql_database import session_maker


def find_device_info_by_device_infos_id(device_info_id: int) -> Maybe[DeviceInfo]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(DeviceInfo)
                                   .filter(DeviceInfo.device_infos_id == device_info_id)
                                   .first()
                                   )

def find_device_info_by_device_id(device_id: str) -> Maybe[DeviceInfo]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(DeviceInfo)
                                   .filter(DeviceInfo.device_id == device_id)
                                   .first()
                                   )

def find_device_info_by_terrorist_id(terrorist_id: str) -> Maybe[DeviceInfo]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(DeviceInfo)
                                   .filter(DeviceInfo.terrorist_id == terrorist_id)
                                   .first())

def create_new_device_info(new_device_info: DeviceInfo) -> DeviceInfo:
    with session_maker() as session:
        session.add(new_device_info)
        session.commit()
        session.refresh(new_device_info)
        return new_device_info
