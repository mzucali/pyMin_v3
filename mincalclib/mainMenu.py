from tkinter import Tk, Frame, Menu



class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()




    def initUI(self):

        self.master.title("Simple menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Mineral Labels", command=print("Hi"))
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)


    def onExit(self):

        self.quit()