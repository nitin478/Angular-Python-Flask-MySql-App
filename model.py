from config import SQLConfig
from sqlalchemy import (Column, Integer, String, ForeignKey, Text, DateTime,
                        Time, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker,relationship
from sql_connector import SqlConnector


Base = declarative_base()


#connector = SqlConnector('root', '10.132.0.3', 'clouddr', password='root')
connector = SqlConnector(
    SQLConfig.USER_ID, SQLConfig.IP, SQLConfig.DB, password=SQLConfig.PASSWORD)
session = connector.get_sql_session()


class Guests(Base):
  __tablename__ = "Guests"
  id = Column(String(50),primary_key=True)
  first = Column(String(20),nullable=False)
  last = Column(String(20),nullable=False)


def AllGuests():
  return session.query(Guests).all()


def UpdateGuest(id, first, last):
  row = session.query(Guests).filter(id == id).first()
  row.first = first
  row.last = last
  session.add(row)
  session.commit()
  return row


def InsertGuest(id, first, last):
  guest = Guests(id=id, first=first, last=last)
  session.add(guest)
  session.commit()
  return guest


"""def DeleteGuest(id):
  key = ndb.Key(Guest, id)
  key.delete()"""
