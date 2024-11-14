from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .terrorist import Terrorist
from .location import Location
from .hostage_sentences import HostageSentence
from .explosive_sentences import ExplosiveSentence
from .device_info import DeviceInfo