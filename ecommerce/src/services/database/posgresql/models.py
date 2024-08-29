from .database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__='user'
    
    user_id=Column(Integer, unique=True, index=True, primary_key=True, autoincrement=True)
    email=Column(String,unique=True, nullable=False)
    password=Column(String,nullable=False)
    name=Column(String)
    phone=Column(String,default=None)
    access_token=Column(String, default=None)
    refresh_token=Column(String, default=None)

