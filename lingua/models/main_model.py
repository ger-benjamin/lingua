from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

SCHEMA = 'main'

class Test(Base):
    __tablename__ = 'test'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
