import tkinter
import tkinter.messagebox

class PizzaGUI:
    def __init__(self):
        # Create main window.
        self.main_window = tkinter.Tk()

        # Size of window
        self.main_window.geometry('300x500')

        # Title of Window
        self.main_window.title('Pizza Builder')


        # Create frames for widgets.
        self.name_frame = tkinter.Frame(self.main_window)
        self.check_button = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)
        self.top_frame = tkinter.Frame(self.main_window)
        self.calc_quit_frame = tkinter.Frame(self.main_window)

#################################################################################################
        # Create widgets for name frame.
        self.name_label = tkinter.Label(self.name_frame,text='Enter your name:')
        self.name_entry = tkinter.Entry(self.name_frame,width=20)

        # Pack the name frame's widgets.
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
#################################################################################################


#################################################################################################
        # Create IntVar for crust radio buttons.
        self.crust_radio_var = tkinter.DoubleVar()

        # Set the crust intVar object to 1.
        self.crust_radio_var.set(1)

        # Create widgets for size frame.
        self.crust_label = tkinter.Label(self.crust_frame,text='Type of Crust:')
        self.crust1 = tkinter.Radiobutton(self.crust_frame,text='Original Crust: $8.99',variable=self.crust_radio_var,value=8.99)
        self.crust2 = tkinter.Radiobutton(self.crust_frame,text='Thin Crust: $10.99',variable=self.crust_radio_var,value=10.99)
        self.crust3 = tkinter.Radiobutton(self.crust_frame,text='NY Style Crust: $11.75',variable=self.crust_radio_var,value=11.75)
        self.crust4 = tkinter.Radiobutton(self.crust_frame,text='Stuffed Crust: $15.89',variable=self.crust_radio_var,value=15.89)

        # Pack the crust frame's widgets.
        self.crust_label.pack(side='top', anchor=tkinter.W)
        self.crust1.pack(side='top', anchor=tkinter.W)
        self.crust2.pack(side='top', anchor=tkinter.W)
        self.crust3.pack(side='top', anchor=tkinter.W)
        self.crust4.pack(side='top', anchor=tkinter.W)
#################################################################################################

#################################################################################################
        # Create meat IntVar objects to use for checkboxes.
        self.top_var1 = tkinter.DoubleVar()
        self.top_var2 = tkinter.DoubleVar()
        self.top_var3 = tkinter.DoubleVar()
        self.top_var4 = tkinter.DoubleVar()
        self.top_var5 = tkinter.DoubleVar()
        self.top_var6 = tkinter.DoubleVar()
        self.top_var7 = tkinter.DoubleVar()
        self.top_var8 = tkinter.DoubleVar()

        # Set meat IntVar objects to 0.
        self.top_var1.set(0)
        self.top_var2.set(0)
        self.top_var3.set(0)
        self.top_var4.set(0)
        self.top_var5.set(0)
        self.top_var6.set(0)
        self.top_var7.set(0)
        self.top_var8.set(0)

        # Create the meat check button widgets.
        self.top_label = tkinter.Label(self.top_frame,text='Choose your toppings:')
        self.top1 = tkinter.Checkbutton(self.top_frame,text='Bacon: +$0.25',variable=self.top_var1)
        self.top2 = tkinter.Checkbutton(self.top_frame,text='Pepperoni: +$0.75',variable=self.top_var2)
        self.top3 = tkinter.Checkbutton(self.top_frame,text='Sausage: +$1.25',variable=self.top_var3)
        self.top4 = tkinter.Checkbutton(self.top_frame,text='Chicken: +$2.00',variable=self.top_var4)
        self.top5 = tkinter.Checkbutton(self.top_frame,text='Tomatoes: +$0.40',variable=self.top_var5)
        self.top6 = tkinter.Checkbutton(self.top_frame,text='Spinach: +$0.25',variable=self.top_var6)
        self.top7 = tkinter.Checkbutton(self.top_frame,text='Bell Peppers: +$1.00',variable=self.top_var7)
        self.top8 = tkinter.Checkbutton(self.top_frame,text='Onions: +$0.60',variable=self.top_var8)

        # Pack the meat check buttons.
        self.top_label.pack(side='top', anchor=tkinter.W)
        self.top1.pack(side='top', anchor=tkinter.W) 
        self.top2.pack(side='top', anchor=tkinter.W) 
        self.top3.pack(side='top', anchor=tkinter.W) 
        self.top4.pack(side='top', anchor=tkinter.W) 
        self.top5.pack(side='top', anchor=tkinter.W) 
        self.top6.pack(side='top', anchor=tkinter.W) 
        self.top7.pack(side='top', anchor=tkinter.W) 
        self.top8.pack(side='top', anchor=tkinter.W) 
#################################################################################################

#################################################################################################
        # Create widgets for calculate and quit buttons.
        self.calc_button = tkinter.Button(self.calc_quit_frame,text='Calculate',command=self.calculate_order)
        self.quit_button = tkinter.Button(self.calc_quit_frame,text='Quit',command=self.main_window.destroy)

        # Pack the button frame's widgets.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
#################################################################################################


        # Pack the frames.
        self.name_frame.pack()
        self.crust_frame.pack()
        self.top_frame.pack()
        self.calc_quit_frame.pack()

        # Enter tkinter main loop.
        tkinter.mainloop()
    

    # Callback function for Button Widget.
    def calculate_order(self):

        # Get the type of crust user selected.
        self.crust = float(self.crust_radio_var.get())

        # Add crust to total cost.
        total = 0 + self.crust

        # Get toppings choice and add amount to total cost.
        if float(self.top_var1.get()) == 1:
            total += 0.25
        if float(self.top_var2.get()) == 1:
            total += 0.75
        if float(self.top_var3.get()) == 1:
            total += 1.25
        if float(self.top_var4.get()) == 1:
            total += 2.00
        if float(self.top_var5.get()) == 1:
            total += 0.40
        if float(self.top_var6.get()) == 1:
            total += 0.25
        if float(self.top_var7.get()) == 1:
            total += 1.00
        if float(self.top_var8.get()) == 1:
            total += 0.60
            
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Order', self.name_entry.get() + '\n' + 'Total: $' + str(format(total, '.2f')))


# Create an instance of the 
pizza = PizzaGUI()