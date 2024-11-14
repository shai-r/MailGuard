from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgresql.models import Base

class ExplosiveSentence(Base):
   __tablename__ = "suspicious_explosive_content"
   hostage_sentence_id = Column(Integer, primary_key=True, autoincrement=True)
   sentence = Column(String)
   terrorist_id = Column(Integer, ForeignKey('terrorists.terrorist_id'))

   terrorist = relationship("Terrorist", back_populates="explosive_sentences")