from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgresql_db.models import Base

class Sentence(Base):
   __tablename__ = "sentences"
   sentence_id = Column(Integer, primary_key=True, autoincrement=False)
   sentence = Column(String)
   terrorist_id = Column(Integer, ForeignKey('terrorists.terrorist_id'))

   terrorist = relationship("Terrorist", back_populates="sentences")