
from postgresdatabase import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    profile = relationship("Profile", back_populates="user")


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    profile_picture = Column(String)
    user = relationship("User", back_populates="profile")

DATABASE_URL = "postgresql://postgres:root123@localhost:5432/registration"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)