# import tkinter as tk
#
# root = Tk()
#
# top_frame = Frame(root)
# top_frame.pack()
# bottom_frame = Frame(root)
# bottom_frame.pack(side=BOTTOM)
#
# button1 = Button(top_frame, text="Button 1", fg="red")
# button2 = Button(top_frame, text="Button 2", fg="blue")
# button3 = Button(top_frame, text="Button 3", fg="green")
# button4 = Button(bottom_frame, text="Button 4", fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)
#
# root.mainloop()

from tkinter import *
master = Tk()
w = Canvas(master, width=800, height=600)
w.pack()
canvas_height=600
canvas_width=780
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )

master.geometry("800x600")

button1 = Button(w, text="Button 1", fg="red")
button2 = Button(w, text="Button 2", fg="blue")
button3 = Button(w, text="Button 3", fg="green")
button4 = Button(w, text="Button 4", fg="purple")

button1.grid(column=1, row=1)
button1.pack()
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


mainloop()
