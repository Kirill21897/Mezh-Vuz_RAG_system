from config.settings import config
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = config.DATABASE_URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Модели/Таблицы

class University(Base):
    __tablename__ = "universities"
    university_id = Column(Integer, primary_key=True)
    name = Column(String(300))
    short_name = Column(String(50))
    city = Column(String(100))
    region = Column(String(100))
    website = Column(String(200))
    email = Column(String(100))
    phone = Column(String(50))
    rating = Column(Numeric(3, 2))
    is_active = Column(Boolean, default=True)
    
    programs = relationship("Program", back_populates="university")
    
    def __repr__(self):
        return f"<University {self.short_name} ({self.city})>"


class Programs(Base):
    __tablename__ = "programs"
    
    program_id = Column(Integer, primary_key=True)
    university_id = Column(Integer, ForeignKey("universities.university_id"))
    name = Column(String(300))
    level = Column(String(50))
    year = Column(String(20))
    type = Column(String(100))
    language = Column(String(50))
    duration = Column(String(100))
    start_date = Column(Date)
    deadline_date = Column(Date)
    requirements = Column(Text)
    quantity = Column(Integer)
    description = Column(Text)
    financing = Column(Text)
    accommodation = Column(String(20))
    is_active = Column(Boolean, default=True)
    
    university = relationship("University", back_populates="programs")
    
    def __repr__(self):
        return f"<Program {self.name[:30]}...>"

# Функции для работы с базой данных

def get_session():
    """Полученние сессию для работы с базой данных"""
    return Session()


def get_all_universities(session):
    """Получение всех активных университетов"""
    return session.query(University).filter(University.is_active == True).all()


def get_university_by_id(session, university_id: int):
    """Получение университета по его ID"""
    with get_session() as session:
        return session.get(University, university_id)
    
def get_all_programs(session):
    """Получение всех активных программ"""
    with get_session() as session:
        return session.query(Programs).join(University).filter(Programs.is_active == True).all()

def get_program_by_university_id(session, university_id: int):
    """Получение всех программ для конкретного университета"""
    with get_session() as session:
        uni = session.get(University, university_id)
        return  uni.programs if uni else []