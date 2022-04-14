from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from projektas_nd1 import Darbuotojas
from datetime import datetime

engine = create_engine('sqlite:///projektai_nd1.db')
Session = sessionmaker(bind=engine)
session = Session()

def person_add():
    while True:
        try:
            f_name = input("Įveskite vardą: ")
            l_name = input("Įveskite pavardę: ")
            b_day = datetime.strptime(input("Įveskite gimimo datą (YYYY-MM-DD): "), "%Y-%m-%d")
            occupation = input("Įveskite pareigas: ")
            salary = float(input("Įveskite atlyginimą: "))
            working_since = datetime.now()
            darbuotojas = Darbuotojas(f_name, l_name, b_day, occupation, salary, working_since)
            session.add(darbuotojas)
            session.commit()
            break
        except:
                print("Klaida. Bandykite dar kartą")

def person_modify():
    pass

def person_del():
    pass

def person_list():
    pass

person_add()




# session = sessionmaker(bind=engine)()

# projektas1 = Projektas("Naujas Projektas", 1000)
# session.add(projektas1)

# projektas2 = Projektas("Rimtesnis Projektas", 5000)
# session.add(projektas2)

# session.commit()

# pirmas = session.query(Projektas).all()
# print(pirmas)
# trecias = session.query(Projektas).filter_by(name="Rimtesnis Projektas").one()
# print(trecias)

#search = session.query(Projektas).filter((Projektas).price > 2000).all()
# print(search)

# search2 = session.query(Projektas).filter(Projektas.name.ilike("%ktas%")).all()
# print(search2)

# updaitai

# irasas = session.query(Projektas).first()
# print(irasas)
# irasas.price = 1300
# session.commit()
# print(irasas)

# session.delete(search)
# session.commit()
# leftovers = session.query(Projektas).all()
# print(leftovers)
