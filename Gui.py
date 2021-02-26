from tkinter import *
from Dispatcher import *

# New Instance Of Dispatcher Class
D = Dispatcher()

# Class to make Gui
class Gui(Frame): 

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Dispatcher (by Cameron Norman)")
        self.pack(fill=BOTH, expand=1)

        # buttons creation and configuration
        populate_queues_button = Button(self, text = "Populate Ready Queue and Blocked List", fg = "black" , bg = "white", command = D.populateReadyQueue())
        populate_queues_button.place(relx = 0.5, rely = 0.2, anchor = CENTER)
        populate_queues_button.config(height = 4, width = 40)

        quit_Button = Button(self, text="QUIT", fg = "black" , bg = "white", command = self.exit)
        quit_Button.place(relx=0.5, rely=0.8, anchor=CENTER)
        quit_Button.config(height = 4, width = 40)

        view_queues_Button = Button(self, text="View ReadyQueue and BlockedList\n(Must Populate First)", fg="black", bg="white", command = D.printQueues)
        view_queues_Button.place(relx=0.5, rely=0.5, anchor=CENTER)
        view_queues_Button.config(height=4, width=40)

    def exit(self):
        exit()

root = Tk()
root.geometry("600x400")

app = Gui(root)
root.mainloop()