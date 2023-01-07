from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, update


class Database1: #Här skapas en superklass som innehåller anslutningen till och själva motorn för databasen

    engine = create_engine('sqlite:///C:\\dbfiles\\mydb39.db')
    #engine = create_engine('sqlite:///C:\\mydb1.db')
    Session = sessionmaker(bind=engine)
    Base = declarative_base()


class Medlem(Database1.Base): #Subklass till Database1 ärver Base

    __tablename__ = 'medlemmar' #Skapar tablet medlemmar med sju stycken attribut per objekt

    id = Column(Integer, primary_key=True)
    förnamn = Column(String)
    efternamn = Column(String)
    gatuadress = Column(String)
    postnummer = Column(Integer)
    postadress = Column(String)
    avgift = Column(String)

    def __init__(self, förnamn, efternamn, gatuadress, postnummer, postadress, avgift):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.gatuadress = gatuadress
        self.postnummer = postnummer
        self.postadress = postadress
        self.avgift = avgift

    @classmethod
    def create_database_table(cls):
        Database1.Base.metadata.create_all(Database1.engine) #Skapar tablet medlemmar i databasen



