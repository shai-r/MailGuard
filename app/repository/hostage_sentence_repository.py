from returns.maybe import Maybe
from typing import Optional

from app.db.postgresql.models import HostageSentence
from app.db.postgresql.postgresql_database import session_maker


def find_hostage_sentence_by_explosive_sentence_id(hostage_sentence_id: int) -> Maybe[
    HostageSentence]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(HostageSentence)
                                   .filter(HostageSentence.hostage_sentence_id == hostage_sentence_id)
                                   .first())


def find_hostage_sentence_by_sentence_and_terrorist_id(sentence: str, terrorist_id: Optional[int] = None) -> Maybe[
    HostageSentence]:
    with session_maker() as session:
        query = session.query(HostageSentence).filter(HostageSentence.sentence == sentence)

        if terrorist_id:
            query = query.filter(HostageSentence.terrorist_id == terrorist_id)

        return Maybe.from_optional(query.first())


def find_hostage_sentence_by_terrorist_id(terrorist_id: str) -> Maybe[HostageSentence]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(HostageSentence)
                                   .filter(HostageSentence.terrorist_id == terrorist_id)
                                   .first()
                                   )


def create_new_hostage_sentence(new_hostage_sentence: HostageSentence) -> HostageSentence:
    with session_maker() as session:
        session.add(new_hostage_sentence)
        session.commit()
        session.refresh(new_hostage_sentence)
        return new_hostage_sentence
