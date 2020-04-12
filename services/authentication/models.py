import datetime

from sqlalchemy import DECIMAL
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    telephone_code = Column(String(10), nullable=True)
    telephone_number = Column(String(10), nullable=True)
    password = Column(String, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )