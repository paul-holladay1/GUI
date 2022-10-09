import tkinter

class myGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Exercise')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)


        self.label1 = tkinter.Label(self.frame1, text = "Enter the score for test 1:")
        self.label2 = tkinter.Label(self.frame2, text = "Enter the score for test 2:")
        self.label3 = tkinter.Label(self.frame3, text = "Enter the score for test 3:")
        self.label4 = tkinter.Label(self.frame4, text = "Average:")

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        self.label4.pack(side='left')


        self.calc_button = tkinter.Button(self.frame5, text="Average\n", command=self.calculate_average)
        self.quitbutton = tkinter.Button(self.frame5, text="Quit\n", command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.entry1 = tkinter.Entry(self.frame1, width=10)
        self.entry2 = tkinter.Entry(self.frame2, width=10)
        self.entry3 = tkinter.Entry(self.frame3, width=10)
        self.entry4 = tkinter.Entry(self.frame4, width=10)

        self.entry1.pack(side='left')
        self.entry2.pack(side='left')
        self.entry3.pack(side='left')
        self.entry4.pack(side='left')

        tkinter.mainloop()

    def calculate_average(self):
        self.test1 = float(self.entry1.get())
        self.test2 = float(self.entry2.get())
        self.test3 = float(self.entry3.get())

        self.calculate_average = float(self.test1 + self.test2 + self.test3) / 3

        self.calculate_average.set(self.calculate_average)

        test_avg = TestAverage()


my_gui = myGUI()

print("I am done!")