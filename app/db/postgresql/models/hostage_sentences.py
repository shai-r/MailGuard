from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgresql.models import Base

class HostageSentence(Base):
   __tablename__ = "suspicious_hostage_content"
   hostage_sentence_id = Column(Integer, primary_key=True, autoincrement=True)
   sentence = Column(String)
   terrorist_id = Column(Integer, ForeignKey('terrorists.terrorist_id'))

   terrorist = relationship("Terrorist", back_populates="hostage_sentences")