from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.postgresql.models import Base

class Terrorist(Base):
   __tablename__ = "terrorists"
   terrorist_id = Column(Integer, primary_key=True, autoincrement=True)
   email = Column(String, unique=True)
   username = Column(String)
   ip_address = Column(String)
   created_at = Column(String)

   hostage_sentences = relationship(
       "HostageSentence",
       back_populates="terrorist",
       cascade="all, delete-orphan"
   )
   explosive_sentences = relationship(
       "ExplosiveSentence",
       back_populates="terrorist",
       cascade="all, delete-orphan"
   )
   location = relationship(
       "Location",
       back_populates="terrorist",
       uselist=False
   )
   device_info = relationship(
       "DeviceInfo",
       back_populates="terrorist",
       uselist=False
   )

