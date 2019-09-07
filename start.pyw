import tkinter as tk
import os


class App():
    def __init__(self, parent):
        parent.title("File Organizer v0.5")
        parent.geometry("420x300+200+100")
        self.selectedDir = os.getcwd()
        self.widgets(parent)

        parent.mainloop()


    def widgets(self, parent):
        self.cdframe = tk.Frame(parent, width=370, height=40, bd=1, relief='raise')
        self.selectedDirText = tk.Label(parent, text=self.selectedDir)
        self.selectedDirText.place(x=30, y=20)
        self.cdframe.place(x=25, y=10)


        self.progressBar = tk.Frame(parent, bg="darkgrey", width=370, height=30)
        tk.Label(parent, text='Progress:').place(x=25, y=228)
        self.progressBar.place(x=25, y=250)

       

    

root = tk.Tk()
main = App(root)