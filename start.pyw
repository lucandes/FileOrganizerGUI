import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

def limitString(string):
    if len(string) > 45:
        return string[:44]+'...'
    else:
        return string

class App():
    def __init__(self, master):
        master.title("File Organizer v0.5")
        master.geometry("420x300+200+100")
        master.resizable(False,False)
        self.master = master
        
        self.dirNames = [
            'Documents', 
            'Compressed', 
            'Torrent', 
            "ISO", 
            'Programs', 
            'Images', 
            'Videos']
        
        self.formats = [
            'txt doc pdf docx lib pdf pptx odt', 
            'zip rar whl deb', 
            'torrent',
            'iso', 
            'py pyw ini msi c cpp java js', 
            'jpg jpeg png gif', 
            'mpeg mp4 mkv', 
            'exe']

        self.selectedDir = ''
        self.widgets(master)

        master.mainloop()


    def widgets(self, master):
        # SELECTED DIR DISPLAY
        self.cdframe = tk.Frame(master, width=370, height=40, bd=1, relief='sunken')
        self.selectedDirText = tk.Label(master, text=limitString(self.selectedDir))
        self.selectedDirText.place(x=35, y=20)
        self.cdframe.place(x=25, y=10)

        # ṔROGRESS BAR
        self.progressBar = tk.Frame(master, bg="darkgrey", width=360, height=30)
        tk.Label(master, text='Progress:').place(x=25, y=228)
        self.progressBar.place(x=25, y=250)

        # BUTTONS
        self.chooseDirBtn = tk.Button(master, text="Select directory", width=19, height=1)
        self.chooseDirBtn['command'] = self.chooseDirBtn_OC
        self.chooseDirBtn.place(x=25, y=55)

        self.getCwdBtn = tk.Button(master, text="Get current", width=19, height=1)
        self.getCwdBtn['command'] = self.getCwdBtn_OC
        self.getCwdBtn.place(x=215, y=55)

        self.editDirNamesBtn = tk.Button(master, text="Edit directories", width=19, height=2)
        self.editDirNamesBtn.place(x=25, y=100)

        self.editFormatsBtn = tk.Button(master, text="Edit formats", width=19, height=2)
        self.editFormatsBtn.place(x=25, y=150)

        self.startBtn = tk.Button(master, text="Start", width=9, height=1)
        self.startBtn.place(x=285, y=215)

        self.cancelBtn = tk.Button(master, text="Cancel", width=9, height=1)
        self.cancelBtn['command'] = master.destroy
        self.cancelBtn.place(x=180, y=215)

        # DIRECTORIES AND FORMATS DISPLAY
        self.editDirVar = tk.StringVar()
        self.editDirCombo = ttk.Combobox(master, textvariable=self.editDirVar, values=self.dirNames)
        self.editDirCombo.bind("<<ComboboxSelected>>", self.getDirIndex)
        self.editDirCombo.current(0)
        self.displayFormList(0)
        self.editDirCombo.place(x=215, y=100)
        
    
    def getDirIndex(self, event):
        selected = self.editDirCombo.current()
        self.displayFormList( selected )
        
    def displayFormList(self, index):
        self.formListBox = tk.Listbox(self.master, height=4, width=21)
        formlist = self.formats[ index].split(" ")

        for i in range(len( formlist )):
            self.formListBox.insert( i, formlist[ i ] )
        self.formListBox.place(x=215, y=122)

    def getCwdBtn_OC(self):
        self.selectedDir = os.getcwd()
        self.selectedDirText['text'] = limitString(self.selectedDir)

    def chooseDirBtn_OC(self):
        temp = tk.filedialog.askdirectory()
        if temp != '':
            self.selectedDir = temp
            self.selectedDirText['text'] = limitString(self.selectedDir)

       

    

root = tk.Tk()
main = App(root)