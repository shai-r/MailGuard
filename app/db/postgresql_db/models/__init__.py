from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .terrorist import Terrorist
from .location import Location
from .sentence import Sentence
from .device_info import DeviceInfo