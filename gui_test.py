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
master.title("Network Reader")
master.geometry("1000x800")

#frames to divide screen
top_frame = Frame(master)
top_frame.pack(side=TOP)

bottom_frame = Frame(master)
bottom_frame.pack(side=BOTTOM)

#labels and textbox to show selected information
#IPv4, Subnet_Mask, Router, Network_name_ Security, Mac_address

ipv4_lb = Label(top_frame, text="IPv4").grid(row=0, column=0)
subnet_mask_lb = Label(top_frame, text="Subnet Mask").grid(row=1, column=0)
router = Label(top_frame, text="Router").grid(row=0, column=2)
network_name = Label(top_frame, text="Network Name").grid(row=1, column=2)
security = Label(top_frame, text="Security").grid(row=0, column=4)
mac_address = Label(top_frame, text="Mac Address").grid(row=1, column=4)


ipv4_tb = Entry(top_frame)
subnet_mask_tb = Entry(top_frame)
router = Entry(top_frame)
network_name = Entry(top_frame)
security = Entry(top_frame)
mac_address = Entry(top_frame)


ipv4_tb.grid(row=0, column=1)
subnet_mask_tb.grid(row=1, column=1)
router.grid(row=0, column=3)
network_name.grid(row=1, column=3)
security.grid(row=0, column=5)
mac_address.grid(row=1, column=5)



#button to execute functions
button1 = Button(bottom_frame, text="Run", fg="red", bg="gray")
button2 = Button(bottom_frame, text="Send to DB", fg="blue", bg="gray")
button3 = Button(bottom_frame, text="Open DB", fg="green", bg="gray")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)


mainloop()
