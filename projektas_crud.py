from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projektas import Projektas

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()
# session = sessionmaker(bind=engine)()

# projektas1 = Projektas("Naujas Projektas", 1000)
# session.add(projektas1)

# projektas2 = Projektas("Rimtesnis Projektas", 5000)
# session.add(projektas2)

session.commit()

# pirmas = session.query(Projektas).all()
# print(pirmas)
# trecias = session.query(Projektas).filter_by(name="Rimtesnis Projektas").one()
# print(trecias)

search = session.query(Projektas).filter((Projektas).price > 2000).all()
# print(search)

search2 = session.query(Projektas).filter(Projektas.name.ilike("%ktas%")).all()
# print(search2)

# updaitai

# irasas = session.query(Projektas).first()
# print(irasas)
# irasas.price = 1300
# session.commit()
# print(irasas)

session.delete(search)
session.commit()
leftovers = session.query(Projektas).all()
print(leftovers)
