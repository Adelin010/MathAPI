# db.py
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()  # type: ignore


# models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    func_name = Column(String, nullable=False)
    nr_params = Column(Integer, nullable=False)
    params_name = Column(String, nullable=False)
    params_value = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
