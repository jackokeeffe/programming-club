from tkinter import *
root = Tk()

check_state = IntVar()
radio_state = StringVar()
scale_state = IntVar()

def print_command():
	# bool(): 0 = False, 1 = True
	print(bool(check_state.get()))
	print(radio_state.get())
	print(scale_state.get())

# New Widgets (Checkbutton, Scale & Radiobutton)

# Checkbutton
Checkbutton(root, text="Check Me", variable=check_state).pack()

# Scale (from_)
# Orientation = CAPS
Scale(root, from_=0, to=10, orient=HORIZONTAL, variable=scale_state).pack()

# print_command NOT print_command()
Button(root, text='Print', command=print_command).pack()

#Radiobuttons
radio = Radiobutton(root, text="First", value="first", variable=radio_state)
radio.pack()

Radiobutton(root, text="Second", value="second", variable=radio_state).pack()

root.mainloop()