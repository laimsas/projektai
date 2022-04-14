from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from bankas import Bankas, Saskaita, Klientas, Likutis
from tkinter import *

engine = create_engine('sqlite:///bankas_db.db')
Session = sessionmaker(bind=engine)
session = Session()


class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x100")
        self.frame = Frame(self.master)
        # scrollbaras = Scrollbar(self.scrollbaras)
        self.left_listbox = Listbox(self.frame, width=30) #, yscrollcommand = self.scrollbaras.set)
        self.right_listbox = Listbox(self.frame, width=30)
        # self.scrollbaras.config(command=self.left_listbox.yview)

        self.left_listbox.grid(row=0, column=0)
        self.right_listbox.grid(row=0, column=1)






        # self.button1 = Button(self.frame, text = "naujas", width =30, command = self.naujas_langas)
        # self.button1.pack()
        # self.frame.pack(side = BOTTOM)

    def naujas_langas(self):
        self.naujas = Toplevel(self.master)
        self.app = Antrinis(self.naujas)

class Antrinis:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x100")
        self.frame = Frame(self.master)
        # self.button1 = Button(self.frame, text = "uzdaryti", command=self.uzdaryti)
        # self.button1.pack()
        # self.frame.pack(side = BOTTOM)

    def uzdaryti(self):
        self.master.destroy()

def main():
    langas = Tk()
    app = Pagrindinis(langas)
    langas.mainloop()

if __name__ == '__main__':
    main()