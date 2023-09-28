from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import Depends

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

ActiveSession = Depends(get_db)

class  MyCrazy:
    def __call__(self) -> None:
        self._db: Session = ActiveSession


