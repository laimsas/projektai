from tkinter import *

class Pagrindinis:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x100")
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text = "naujas", width =30, command = self.naujas_langas)
        self.button1.pack()
        self.frame.pack(side = BOTTOM)

    def naujas_langas(self):
        self.naujas = Toplevel(self.master)
        self.app = Antrinis(self.naujas)

class Antrinis:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x100")
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text = "uzdaryti", command=self.uzdaryti)
        self.button1.pack()
        self.frame.pack(side = BOTTOM)

    def uzdaryti(self):
        self.master.destroy()

def main():
    langas = Tk()
    app = Pagrindinis(langas)
    langas.mainloop()

if __name__ == '__main__':
    main()