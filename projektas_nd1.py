from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///projektai_nd1.db')
Base = declarative_base()

class Darbuotojas(Base):
    __tablename__ = 'Darbuotojai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column("first name", String)
    l_name = Column("last name", String)
    b_day = Column("birthday", DateTime) 
    occupation = Column("Occupation", String)
    sallary = Column("Salary", Float)
    works_since = Column("Since", DateTime, default=datetime.utcnow)

    def __init__(self, f_name, l_name, b_day, occupation, sallary, works_since):  
        self.f_name = f_name
        self.l_name = l_name
        self.b_day = b_day
        self.occupation = occupation
        self.sallary = sallary
        self.works_since = works_since

    def __repr__(self):
        return f"{self.id} : {self.f_name} {self.l_name} : {self.b_day} : {self.occupation} : {self.sallary} : {self.works_since}"

Base.metadata.create_all(engine)