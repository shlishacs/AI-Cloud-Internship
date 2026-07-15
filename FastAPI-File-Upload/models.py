from sqlalchemy import Column, Integer, String, BigInteger, Text, TIMESTAMP
from sqlalchemy.sql import func
from database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))
    file_type = Column(String(100))
    file_size = Column(BigInteger)
    file_path = Column(Text)
    uploaded_at = Column(TIMESTAMP(timezone=True), server_default=func.now())