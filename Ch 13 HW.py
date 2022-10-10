import tkinter
import tkinter.messagebox

class PizzaGUI:
    def __init__(self):
        # Create main window.
        self.main_window = tkinter.Tk()

        # Create frames for widgets.
        self.name_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.check_button = tkinter.Frame(self.main_window)
        self.calc_quit_frame = tkinter.Frame(self.main_window)

        # Create widgets for name frame.
        self.name_label = tkinter.Label(self.name_frame,text='Enter your name:')
        self.name_entry = tkinter.Entry(self.name_frame,width=10)

        # Pack the name frame's widgets.
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        # Create IntVar for size Radio Buttons.
        self.size_radio_var = tkinter.IntVar()

        # Set the intVar object to 1.
        self.size_radio_var.set(1)

        # Create widgets for size frame.
        self.size1 = tkinter.Radiobutton(self.size_frame,text='Small',variable=self.size_radio_var,value='Small')
        self.size2 = tkinter.Radiobutton(self.size_frame,text='Medium',variable=self.size_radio_var,value='Medium')
        self.size3 = 
        # Pack the size frame's widgets.

        # Create widget for check button frame.
        self.button = tkinter.Button(self.main_window,text='OK',command=self.do_something)

        # Pack the check button
        self.button.pack(side='bottom')








        # # Create widgets for calculate and quit buttons.
        # self.calc_button = tkinter.Button(self.calc_quit_frame,text='Calculate',command=self.calculate)
        # self.quit_button = tkinter.Button(self.calc_quit_frame,text='Quit',command=self.main_window.destroy)

        # # Pack the button frame's widgets.
        # self.calc_button.pack(side='left')
        # self.quit_button.pack(side='left')

        # Pack the frames.
        self.name_frame.pack()
        self.calc_quit_frame.pack()
        self.check_button.pack()

        # Enter tkinter main loop.
        tkinter.mainloop()

    # Callback function for Button Widget
    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Order', self.name_entry.get())

# Create an instance of the 
pizza = PizzaGUI()