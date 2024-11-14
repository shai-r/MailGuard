from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgresql_db.models import Base

class Terrorist(Base):
   __tablename__ = "terrorists"
   terrorist_id = Column(Integer, primary_key=True, autoincrement=False)
   email = Column(String)
   username = Column(Integer, ForeignKey('countries.country_id'))
   ip_address = Column(String)
   created_at = Column(String)

   sentences = relationship(
       "Sentence",
       back_populates="terrorist",
       cascade="all, delete-orphan"
   )
   location = relationship(
       "Location",
       back_populates="terrorists",
       uselist=False
   )
   device_info = relationship(
       "DeviceInfo",
       back_populates="terrorists",
       uselist=False
   )

