from tkinter import *
import tkinter as tk
import sys
from Project2 import *
from FreeSpace import *

# New Instance Of Dispatcher Class
D = Dispatcher()
F = FreeMemory()
# Class to make Gui
class Gui(Frame): 

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Dispatcher Simulation (by Cameron Norman)")
        self.pack(fill=BOTH, expand=1)

        # buttons creation and configuration
        populate_queues_button = Button(self, text = "Populate Process Request", fg = "black" , bg = "#4682B4", command = D.populateProcessRequest)
        populate_queues_button.place(relx = 0.2, rely = 0.15, anchor = CENTER)
        populate_queues_button .config(height = 4, width = 20)

        add_process_button = Button(self, text = "Display Process Request", fg = "black" , bg = "#4682B4", command = D.displayProcessRequest)
        add_process_button.place(relx = 0.2, rely = 0.5, anchor = CENTER)
        add_process_button.config(height = 4, width = 20)

        remove_process_button = Button(self, text = "Display Free Memory", fg = "black" , bg = "#4682B4", command = F.displayFreeSpace)
        remove_process_button.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        remove_process_button.config(height = 4, width = 20)

        populate_memory_button = Button(self, text = "Populate Free Memory", fg = "black" , bg = "#4682B4", command = F.populateFreeMemory)
        populate_memory_button.place(relx = 0.5, rely = 0.15, anchor = CENTER)
        populate_memory_button.config(height = 4, width = 20)

        quit_Button = Button(self, text="QUIT", fg = "black" , bg = "#4682B4", command = self.exit)
        quit_Button.place(relx=0.8, rely=0.8, anchor=CENTER)
        quit_Button.config(height = 4, width = 20)

        display_mem = Button(self, text="Display Active Memory", fg = "black" , bg = "#4682B4", command = D.DisplayRunningMemory)
        display_mem.place(relx=0.5, rely=0.8, anchor=CENTER)
        display_mem.config(height = 4, width = 20)

        view_queues_Button = Button(self, text="Allocate Processes", fg="black", bg="#4682B4", command = D.allocate)
        view_queues_Button.place(relx=0.8, rely=0.15, anchor=CENTER)
        view_queues_Button.config(height=4, width=20)

        context_switch_Button = Button(self, text="De-Allocate Processes", fg="black", bg="#4682B4", command = D.deallocate)
        context_switch_Button.place(relx=0.8, rely=0.5, anchor=CENTER)
        context_switch_Button.config(height=4, width=20)
    def exit(self):
        exit()

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
        self.textbox.see("end")    # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass

root = Tk()
root.geometry("600x400")

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

t = tk.Text(bg="#4682B4", fg="black", height=8.5, width=70, yscrollcommand=scroll.set,)
t.pack()

pl = PrintLogger(t)
sys.stdout = pl

app = Gui(root)
root.mainloop()