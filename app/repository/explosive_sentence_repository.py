from returns.maybe import Maybe
from typing import Optional

from app.db.postgresql.models import ExplosiveSentence
from app.db.postgresql.postgresql_database import session_maker


def find_explosive_sentence_by_explosive_sentence_id(explosive_sentence_id: int) -> Maybe[
    ExplosiveSentence]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(ExplosiveSentence)
                                   .filter(ExplosiveSentence.explosive_sentence_id == explosive_sentence_id)
                                   .first())


def find_explosive_sentence_by_sentence_and_terrorist_id(sentence: str, terrorist_id: Optional[int] = None) -> Maybe[
    ExplosiveSentence]:
    with session_maker() as session:
        query = session.query(ExplosiveSentence).filter(ExplosiveSentence.sentence == sentence)

        if terrorist_id:
            query = query.filter(ExplosiveSentence.terrorist_id == terrorist_id)

        return Maybe.from_optional(query.first())


def find_explosive_sentence_by_terrorist_id(terrorist_id: str) -> Maybe[ExplosiveSentence]:
    with session_maker() as session:
        return Maybe.from_optional(session
                                   .query(ExplosiveSentence)
                                   .filter(ExplosiveSentence.terrorist_id == terrorist_id)
                                   .first()
                                   )


def create_new_explosive_sentence(new_explosive_sentence: ExplosiveSentence) -> ExplosiveSentence:
    with session_maker() as session:
        session.add(new_explosive_sentence)
        session.commit()
        session.refresh(new_explosive_sentence)
        return new_explosive_sentence
