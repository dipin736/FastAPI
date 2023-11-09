from sqlalchemy import Column, String, Integer
from postgresdatabase import Base
from sqlalchemy import create_engine

class PostgresUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)

DATABASE_URL = "postgresql://postgres:root123@localhost:5432/userdb"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)