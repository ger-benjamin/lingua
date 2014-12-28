from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

SCHEMA = 'main'

class Voc(Base):
    __tablename__ = 'voc'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

class Word(Base):
    __tablename__ = 'word'
    __table_args__ = {'schema': SCHEMA}
    id = Column(Integer, primary_key=True)
    id_voc = Column(Integer, ForeignKey("main.voc.id"), nullable=False)

class Word_fr(Base):
    __tablename__ = 'word_fr'
    __table_args__ = {'schema': SCHEMA}
    id_word_fr = Column(Integer, primary_key=True)
    id_word = Column(Integer, ForeignKey("main.word.id"), nullable=False)
    kind = Column(String(15))
    word = Column(Text)
    vari = Column(String(30))

class Word_de(Base):
    __tablename__ = 'word_de'
    __table_args__ = {'schema': SCHEMA}
    id_word_de = Column(Integer, primary_key=True)
    id_word = Column(Integer, ForeignKey("main.word.id"), nullable=False)
    kind = Column(String(15))
    word = Column(Text)
    vari = Column(String(30))
