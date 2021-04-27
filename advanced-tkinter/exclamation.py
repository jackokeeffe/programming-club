'''
Challenge:
- Add a checkbox with a variable to the GUI.
- If checkbox is checked, add an exclamation mark to the entered string.
'''

from tkinter import *

def print_entry():
	# check_state.get() is way to see state of checkbutton
	if check_state.get() == 1:
		# Add ! to e1 (entry) string
		print(e1.get() + "!")
	else:
		# If checkbutton isn't clicked, dont add anything
		print(e1.get())

root = Tk()
entry_text = str()

# IntVar() allows us to use .get()
check_state = IntVar()

Label(root, text='Message: ').pack()
e1 = Entry(root)
e1.pack()

Checkbutton(root, text="Check Me", variable=check_state).pack(side=LEFT)
Button(root, text="Click Me", command=print_entry).pack()

root.mainloop()