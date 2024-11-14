from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.postgresql.models import Base

class Location(Base):
   __tablename__ = "locations"
   location_id = Column(Integer, primary_key=True, autoincrement=False)
   latitude = Column(Float)
   longitude = Column(Float)
   city = Column(String)
   country = Column(String)
   terrorist_id = Column(Integer, ForeignKey('terrorists.terrorist_id'))

   terrorist = relationship(
       "Terrorist",
       back_populates="locations",
       uselist=False
   )
