from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import  sessionmaker, DeclarativeBase, Mapped, mapped_column


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

DATABASE_URL = "postgresql+psycopg2://postgres:ExploitX2107+try@localhost:5432/classroom_db"
engine = create_engine(DATABASE_URL)

SessinLocal = sessionmaker(autocommit=False, autoflush=False, bind=DATABASE_URL)


