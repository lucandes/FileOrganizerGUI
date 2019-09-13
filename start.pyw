import tkinter as tk
from tkinter import ttk
import os

def limitString(string):
    if len(string) > 45:
        return string[:44]+'...'
    else:
        return string

class App():
    def __init__(self, parent):
        parent.title("File Organizer v0.5")
        parent.geometry("420x300+200+100")
        parent.resizable(False,False)

        self.dirNames = ['Documents', 'Compressed', 'Torrent', "ISO", 'Programs', 'Images', 'Videos']
        self.selectedDir = os.getcwd()
        self.widgets(parent)

        parent.mainloop()


    def widgets(self, parent):
        # SELECTED DIR DISPLAY
        self.cdframe = tk.Frame(parent, width=370, height=40, bd=1, relief='sunken')
        self.selectedDirText = tk.Label(parent, text=limitString(self.selectedDir))
        self.selectedDirText.place(x=35, y=20)
        self.cdframe.place(x=25, y=10)

        # ṔROGRESS BAR
        self.progressBar = tk.Frame(parent, bg="darkgrey", width=360, height=30)
        tk.Label(parent, text='Progress:').place(x=25, y=228)
        self.progressBar.place(x=25, y=250)

        # BUTTONS
        self.chooseDirBtn = tk.Button(parent, text="Select directory", width=19, height=1)
        self.chooseDirBtn.place(x=25, y=55)

        self.getCwdBtn = tk.Button(parent, text="Get current", width=19, height=1)
        self.getCwdBtn.place(x=215, y=55)

        self.editDirNamesBtn = tk.Button(parent, text="Edit directories", width=19, height=2)
        self.editDirNamesBtn.place(x=25, y=100)

        self.editFormatsBtn = tk.Button(parent, text="Edit formats", width=19, height=2)
        self.editFormatsBtn.place(x=25, y=150)

        self.startBtn = tk.Button(parent, text="Start", width=9, height=1)
        self.startBtn.place(x=285, y=215)

        self.cancelBtn = tk.Button(parent, text="Cancel", width=9, height=1)
        self.cancelBtn.place(x=180, y=215)

        # DIRECTORIES DISPLAY
        self.editDirVar = tk.StringVar()
        self.editDirCombo = ttk.Combobox(parent, textvariable=self.editDirVar, values=self.dirNames)
        self.editDirCombo.current(0)
        self.editDirCombo.place(x=215, y=100)

        # FORMATS DISPLAY
        self.formListBox = tk.Listbox(parent, height=4, width=21)
        for i in range(len(self.dirNames)):
            self.formListBox.insert( i, self.dirNames[ i ] )
        self.formListBox.place(x=215, y=122)


       

    

root = tk.Tk()
main = App(root)