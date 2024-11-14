from sqlalchemy import column

from app.db.postgresql.models import Terrorist
from app.db.postgresql.postgresql_database import session_maker
from app.repository.terrorist_repository import find_terrorist_by_email


def get_all_terrorist_by_email(email: str):
    with session_maker() as session:
        r = session.merge(find_terrorist_by_email(email))
        w = {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
        p = {**w,
            'location': {
                'latitude': r.location.latitude,
                'longitude': r.location.longitude,
                'city': r.location.city,
                'country': r.location.country,
            },
            'device_info': {
                'os': r.device_info.os,
                'device_id': r.device_info.device_id,
            },
            'explosive_sentences': [s.sentence for s in r.explosive_sentences] or [],
            'hostage_sentences': [s.sentence for s in r.hostage_sentences] or []
        }
        print(p)
        return p
