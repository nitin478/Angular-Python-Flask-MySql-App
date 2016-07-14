from config import SQLConfig
from sqlalchemy import (Column, Integer, String, ForeignKey, Text, DateTime,
                        Time, Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sql_connector import SqlConnector


Base = declarative_base()


#connector = SqlConnector('root', '10.132.0.3', 'clouddr', password='root')
connector = SqlConnector(
    SQLConfig.USER_ID, SQLConfig.IP, SQLConfig.DB, password=SQLConfig.PASSWORD)



class Guests(Base):
    __tablename__ = "Guests"
    id = Column(String(50),primary_key=True)
    first = Column(String(20),nullable=False)
    last = Column(String(20),nullable=False)


def AllGuests():
    session = connector.get_sql_session()
    result = session.query(Guests).all()
    session.close()
    return result


def UpdateGuest(id, first, last):
    session = connector.get_sql_session()
    row = session.query(Guests).filter(id == id).first()
    row.first = first
    row.last = last
    session.add(row)
    session.commit()
    session.close()
    return row


def InsertGuest(id, first, last):
    session = connector.get_sql_session()
    guest = Guests(id=id, first=first, last=last)
    session.add(guest)
    session.commit()
    session.close()
    return guest


def DeleteGuest(id):
    session = connector.get_sql_session()
    row = session.query(Guests).filter(id == id).first()
    session.add(row)
    session.commit()
    session.close()
