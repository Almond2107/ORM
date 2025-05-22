from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import  sessionmaker, DeclarativeBase, Mapped, mapped_column
import os

from dotenv import load_dotenv

load_dotenv()





class Base(DeclarativeBase):
    pass

class Student(Base):

    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    fname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column()

class Professor(Base):

    __tablename__ = "professor"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    fname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)

class Course(Base):

    __tablename__ = "course"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[int] = mapped_column()

class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_HOST = os.getenv("DB_HOST")

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

SessinLocal = sessionmaker(autocommit=False, autoflush=False, bind=DATABASE_URL)


