from typing import List

from returns.maybe import Maybe
from sqlalchemy.orm import joinedload

from app.db.postgresql.models import Terrorist
from app.db.postgresql.postgresql_database import session_maker


def find_terrorist_by_id(terrorist_id: int) -> Maybe[Terrorist]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(Terrorist)
                                   .filter(Terrorist.terrorist_id == terrorist_id)
                                   .first())

def find_terrorist_by_email(terrorist_email: str='williamsroberta@example.org') -> Maybe[Terrorist]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Terrorist).options(
            joinedload(Terrorist.explosive_sentences),
            joinedload(Terrorist.hostage_sentences),
            joinedload(Terrorist.location),
            joinedload(Terrorist.device_info)
        ).filter(Terrorist.email == terrorist_email).first())

def find_terrorists_by_username(terrorist_username: str) -> List[Terrorist]:
    with session_maker() as session:
        return session.query(Terrorist).filter(Terrorist.username == terrorist_username)

def create_new_terrorist_if_not_exists(new_terrorist: Terrorist) -> Maybe[Terrorist]:
    terrorist_exists = find_terrorist_by_email(new_terrorist.email).value_or(None)
    if terrorist_exists:
        return Maybe.from_optional(None)
    with session_maker() as session:
        session.add(new_terrorist)
        session.commit()
        session.refresh(new_terrorist)
        return Maybe.from_optional(new_terrorist)
