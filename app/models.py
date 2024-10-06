from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer,String,Boolean,text
from .database import Base

class IotDevices(Base):
    __tablename__ = "IotDevices"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    type = Column(String,nullable=False)
    created_time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 
    state = Column(Boolean,nullable=False,server_default='False')
class User(Base):
    __tablename__ = "users"
    email = Column(String,unique=True,nullable=False)
    username = Column(String,primary_key=True,nullable=False)
    password = Column(String,nullable=False)
    admin = Column(Boolean,nullable=False,server_default='False')
    created_time = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')) 
