import tkinter as tk


class App():
    def __init__(self, parent):
        parent.title("File Organizer v0.5")
        parent.geometry("400x300+200+100")
        self.widgets(parent)

        parent.mainloop()


    def widgets(self, parent):
        self.cdf = tk.Frame(parent, width=360, height=30, relief='raise', fg=1)
        self.cdf.place(x=20, y=10)

       

    

root = tk.Tk()
main = App(root)