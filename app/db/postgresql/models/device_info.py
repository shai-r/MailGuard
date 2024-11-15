from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.postgresql.models import Base

class DeviceInfo(Base):
   __tablename__ = "devices_info"
   device_info_id = Column(Integer, primary_key=True, autoincrement=True)
   browser = Column(String)
   os = Column(String)
   device_id = Column(String)
   terrorist_id = Column(Integer, ForeignKey('terrorists.terrorist_id'))

   terrorist = relationship(
       "Terrorist",
       back_populates="device_info",
       uselist=False
   )