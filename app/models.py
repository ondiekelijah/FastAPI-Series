from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.sql import func


from .database import Base

# create a class that represents a table in a SQL

class Post(Base):
    __tablename__ = "posts"

    id = Column("id",Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
