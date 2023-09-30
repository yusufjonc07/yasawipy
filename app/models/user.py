from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from app.db import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String(255), nullable=False)
    username = Column(String(20), nullable=False)
    password_hashed = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=True)
    roles = Column(String(255), nullable=True)
    status = Column(Integer, nullable=False, default=10)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
   

