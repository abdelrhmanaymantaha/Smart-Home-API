from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime


class User(BaseModel):
     email: EmailStr
     username: str
     password: str
     admin: bool

class UserOut(BaseModel):
     email: EmailStr
     username: str
     created_time: datetime
     admin: bool

class AddedSensor(BaseModel):
     id: int
     name: str
     type: str


class SensorOut(AddedSensor):
     state: bool
     created_time: datetime

class SensorUpdateState(BaseModel):
     state: Optional[bool]

class UserData(BaseModel):
     username: str
     admin: bool

class Token(BaseModel):
    access_token : str
    token_type : str
    user_data: UserData

class TokenData(BaseModel):
    username:Optional[str] = None
    admin:Optional[bool] = False

class UserLogin(BaseModel):
    email:EmailStr
    password:str
     
