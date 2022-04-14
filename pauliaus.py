from tkinter import *

class Vehicle:
 
    def __init__(self, make, model, prod_year, fuel, unit_value):
        self.make = make
        self.model = model
        self.prod_year = prod_year
        self.fuel = fuel
        self.unit_value = unit_value
    
    def __str__(self):  
        return f"{self.make}: {self.model} {self.prod_year} {self.fuel} {self.unit_value}"

class Catalog:
    unit_list = []

    def add_vehicle(self, vehicle):
        self.unit_list.append(vehicle)

    def show_records(self):
        for i in self.unit_list:
            print(i)

    def total_value(self):
        pass

class Langas:

    def __init__(self):
        self.katalogas = Catalog()
        self.p_window = Tk()
        self.p_window.geometry("300x300")
    
        self.lbl_make = Label(self.p_window, text = "Markė")
        self.lbl_model = Label(self.p_window, text ="Modelis")
        self.lbl_year = Label(self.p_window, text="Gamybos metai")
        self.lbl_fuel = Label(self.p_window, text="Kuro tipas")
        self.lbl_value = Label(self.p_window, text="Kaina")
        self.fld_make = Entry(self.p_window)
        self.fld_model = Entry(self.p_window)
        self.fld_year = Entry(self.p_window)
        self.fld_fuel = Entry(self.p_window)
        self.fld_value = Entry(self.p_window)

        self.myg1 = Button(text = "Naujas")
        self.myg2 = Button(text = "Išsaugoti")
        self.myg3 = Button(text = "Išvalyti")
        self.myg2.bind("<Button-1>", lambda event: self.add_vehicle())
        self.myg1.bind("<Button-1>", lambda event: self.show_records())

        self.lbl_make.grid(row=0, column=0, sticky =E)
        self.lbl_model.grid(row=1, column=0, sticky =E)
        self.lbl_year.grid(row=2, column=0, sticky =E)
        self.lbl_fuel.grid(row=3, column=0, sticky =E)
        self.lbl_value.grid(row=4, column=0, sticky =E)

        self.fld_make.grid(row=0, column=1)
        self.fld_model.grid(row=1, column=1)
        self.fld_year.grid(row=2, column=1)
        self.fld_fuel.grid(row=3, column=1)
        self.fld_value.grid(row=4, column=1)

        self.myg1.grid(row=1, column=3)
        self.myg2.grid(row=2, column=3)
        self.myg3.grid(row=3, column=3)

        self.meniukstis = Menu(self.p_window)
        self.p_window.config(menu = self.meniukstis)

        self.submeniukas = Menu(self.meniukstis, tearoff=False)

        self.meniukstis.add_cascade(label="Meniu", menu =self.submeniukas)

        # submeniukas.add_command(label = "išvalyti", command=valyti)
        # submeniukas.add_command(label = "atkurti", command=atkurti)
        # submeniukas.add_separator()
        # submeniukas.add_command(label = "išeiti", command=iseiti)
    
    def show_records(self):
        self.katalogas.show_records()

    def add_vehicle(self):
        self.katalogas.add_vehicle(Vehicle(self.fld_make.get(), self.fld_model.get(), self.fld_year.get(), self.fld_fuel.get(), self.fld_value.get()))
        print(self.katalogas.unit_list[-1])



langas = Langas()
langas.p_window.mainloop()
