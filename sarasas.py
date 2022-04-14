from tkinter import *

def rodyti():
    rezultatas['text'] = sarasas[saraso_deze.curselection()[0]]

langas = Tk()
langas.geometry("400x200")
scrollbaras = Scrollbar(langas)
saraso_deze = Listbox(langas, width=30, yscrollcommand = scrollbaras.set)
scrollbaras.config(command=saraso_deze.yview)
sarasas = ["1sar1", "1sar2", "1sar3" ]
sarasas2 = ["bla", "bla", "bla" ]
saraso_deze.insert(0, *sarasas)
saraso_deze.insert(1, *sarasas2)

but =Button(langas, text="Rodyti", command=rodyti)
rezultatas = Label(langas)

saraso_deze.pack(side=LEFT)
scrollbaras.pack(side=RIGHT, fill=Y)

but.pack(side = BOTTOM)
rezultatas.pack(side = BOTTOM)

langas.mainloop()