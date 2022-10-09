# # 13-1 (empty_wondow1.py)

# # This program displays an empty window.
# import tkinter                                  

# def main():
#     # Create the main window widget.
#     main_window = tkinter.Tk()

#     # Enter the tkinter main loop.
#     tkinter.mainloop()

# # Call the main function.
# main()


#13-2 (empty_window2.py)

# This program displays an empty window.

# import tkinter

# class MyGUI:
#     def __init__(self):
#         # Create the main window widget.
#         self.main_window = tkinter.Tk()

#         # Enter the tkinter main loop.
#         tkinter.mainloop()

# # Create an instance of the MyGUI class.
# my_gui = MyGUI()


# 13-3 (hello_world.py)

# This program displays a lable with text

# import tkinter

# class MyGUI:
#     def __init__(self):
#         # Create thee main window widget.
#         self.main_window = tkinter.Tk()

#         # Create a Label widget containing this text 'Hello World'
#         self.label = tkinter.Label(self.main_window, text='Hello World')

#         # Call the Label widget's pack method.
#         self.label.pack()

#         # Enter the tkinter main loop.
#         tkinter.mainloop()

# # Create an instance of the MyGUI class.
# my_gui = MyGUI()


# 13-4 (hello_world2.py)

# This program displays two labels with text.

# import tkinter

# class MyGUI:
#     def __init__(self):
#         # Create the main window widget.
#         self.main_window = tkinter.Tk()

#         # Create two Label widgets.
#         self.label1 = tkinter.Label(self.main_window, text='Hello World!')
#         self.label2 = tkinter.Label(self.main_window, text='This is my GUI program.')

#         # Call both Label widgets' pack method.
#         self.label1.pack()
#         self.label2.pack()

#         # Enter the tkinter main loop.
#         tkinter.mainloop()

# # Create an instance of the MyGUI class.
# my_gui = MyGUI()


# 13-5 (hello_world3.py)

# This program uses the side='left' argument with
# the pack method to change the layout of the widgets.

# import tkinter

# class MyGUI:
#     def __init__(self):
#         # Create the main window widget.
#         self.main_window = tkinter.Tk()

#         # Create two Label widgets
#         self.label1 = tkinter.Label(self.main_window, text='Hello world!')
#         self.label2 = tkinter.Label(self.main_window, text='This is my GUI program.')

#         # Call both Label widgets' pack method.
#         self.label1.pack(side='left')
#         self.label2.pack(side='left')

#         # Enter the tkinter main loop.
#         tkinter.mainloop()

# # Create an instance of the MyGUI class
# my_gui = MyGUI()


# 13-6 (frame_demo.py)



