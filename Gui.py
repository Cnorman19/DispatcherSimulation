from tkinter import *
from Dispatcher import *
import tkinter as tk
import sys

# New Instance Of Dispatcher Class
D = Dispatcher()

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
        populate_queues_button = Button(self, text = "Populate Ready Queue \nand Blocked List", fg = "black" , bg = "#4682B4", command = D.populateReadyQueue)
        populate_queues_button.place(relx = 0.8, rely = 0.15, anchor = CENTER)
        populate_queues_button .config(height = 4, width = 20)

        add_process_button = Button(self, text = "Add Process", fg = "black" , bg = "#4682B4", command = D.addProcess)
        add_process_button.place(relx = 0.2, rely = 0.15, anchor = CENTER)
        add_process_button.config(height = 4, width = 20)

        remove_process_button = Button(self, text = "Remove Process", fg = "black" , bg = "#4682B4", command = D.removeProcess)
        remove_process_button.place(relx = 0.5, rely = 0.15, anchor = CENTER)
        remove_process_button.config(height = 4, width = 20)

        quit_Button = Button(self, text="QUIT", fg = "black" , bg = "#4682B4", command = self.exit)
        quit_Button.place(relx=0.5, rely=0.89, anchor=CENTER)
        quit_Button.config(height = 2, width = 40)

        view_queues_Button = Button(self, text="View ReadyQueue and BlockedList", fg="black", bg="#4682B4", command = D.printQueues)
        view_queues_Button.place(relx=0.5, rely=0.45, anchor=CENTER)
        view_queues_Button.config(height=4, width=40)

        context_switch_Button = Button(self, text="Perform Context Switch\n(Scroll up to see output before contextSwitch)", fg="black", bg="#4682B4", command = D.contextSwitch)
        context_switch_Button.place(relx=0.5, rely=0.7, anchor=CENTER)
        context_switch_Button.config(height=3, width=40)

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