from tkinter import *

def spausdinti(event):
    print("Spausdina")
    rezultatas['text'] = f"Hi {laukas_uzr1.get()} {laukas_uzr2.get()}"
def spausdinti_desini(event):
    print("desinis")
def spausdinti_enter(event):
    print("enter")
def vardas(event):
    print(laukas_uzr1.get())
    rezultatas['text'] = f"Hi {laukas_uzr1.get()}"
def pavarde(event):
    print(laukas_uzr2.get())
    rezultatas['text'] = f"Hi {laukas_uzr2.get()}"

langas = Tk()
uzr1 = Label(langas, text = "vardas")
uzr2 = Label(langas, text ="pavarde")
laukas_uzr1 = Entry(langas)
laukas_uzr2 = Entry(langas)
varnele_sutinku = Checkbutton(langas, text ="Man viskas tinka")
mygtukukas_tvirtinti =Button(langas, text="Tvirtinu")
mygtukukas_tvirtinti.bind("<Button-1>", vardas)
mygtukukas_tvirtinti.bind("<Button-2>", spausdinti)
mygtukukas_tvirtinti.bind("<Button-3>", pavarde)
mygtukukas_tvirtinti.bind("<Return>", spausdinti_enter)

rezultatas = Label(langas, text = "")

uzr1.grid(row=0, column=0, sticky =E)
laukas_uzr1.grid(row=0, column=1)
uzr2.grid(row=1, column=0, sticky =E)
laukas_uzr2.grid(row=1, column=1)
varnele_sutinku.grid(row=2, column=2)
mygtukukas_tvirtinti.grid(row=3, columnspan=2)
rezultatas.grid(row=4, columnspan=2)

langas.mainloop()