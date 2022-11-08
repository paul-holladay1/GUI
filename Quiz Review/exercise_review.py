import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title("Average Grade")

        self.test1frame = tkinter.Frame(self.main_window)
        self.test2frame = tkinter.Frame(self.main_window)
        self.test3frame = tkinter.Frame(self.main_window)
        self.avgframe = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.test1frame, text='Enter the score for test 1:')
        self.entry1 = tkinter.Entry(self.test1frame, width=10)

        self.label1.pack(side='left')
        self.entry1.pack(side='left')

        self.label2 = tkinter.Label(self.test2frame, text='Enter the score for test 2:')
        self.entry2 = tkinter.Entry(self.test2frame, width=10)

        self.label2.pack(side='left')
        self.entry2.pack(side='left')

        self.label3 = tkinter.Label(self.test3frame, text='Enter the score for test 3:')
        self.entry3 = tkinter.Entry(self.test3frame, width=10)

        self.label3.pack(side='left')
        self.entry3.pack(side='left')

        self.result_label = tkinter.Label(self.avgframe, text='Average:')
        self.average = tkinter.StringVar()
        







        self.test1frame.pack()
        self.test2frame.pack()
        self.test3frame.pack()

        tkinter.mainloop()

my_gui = myGUI()

