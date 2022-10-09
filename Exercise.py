import tkinter

class TestAverage:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Exercise')

        self.score1_frame = tkinter.Frame(self.main_window)
        self.score2_frame = tkinter.Frame(self.main_window)
        self.score3_frame = tkinter.Frame(self.main_window)
        self.average_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.score1_label = tkinter.Label(self.score1_frame, text='Enter the score for teest1:')
        self.score1_entry = tkinter.Entry(self.score1_frame, width=10)
        self.score1_label.pack(side='left')
        self.score1_entry.pack(side='left')

        self.score2_label = tkinter.Label(self.score2_frame, text='Enter the score for teest2:')
        self.score2_entry = tkinter.Entry(self.score2_frame, width=10)
        self.score2_label.pack(side='left')
        self.score2_entry.pack(side='left')

        self.score3_label = tkinter.Label(self.score3_frame, text='Enter the score for teest3:')
        self.score3_entry = tkinter.Entry(self.score3_frame, width=10)
        self.score3_label.pack(side='left')
        self.score3_entry.pack(side='left')

        self.result_label = tkinter.Label(self.average_frame, text='Average')
        self.average = tkinter.StringVar()
        self.average_label = tkinter.Label(self.average_frame, textvariable=self.average)
        self.result_label.pack(side='left')
        self.average_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame, text='Average', command=self.calculate_average)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.score1_frame.pack()
        self.score2_frame.pack()
        self.score3_frame.pack()
        self.average_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calculate_average(self):
        self.score1 = float(self.score1_entry.get())
        self.score2 = float(self.score2_entry.get())
        self.score3 = float(self.score3_entry.get())

        self.average.set(float((self.score1 + self.score2 + self.score3) / 3.0))

test_avg = TestAverage()

