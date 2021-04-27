from tkinter import *

# Define root frame
root = Tk()

# Define variables needed
entry_text = str()

# Define what to do when button is clicked
def print_entry():
	print(e1.get())

# Add label in root frame
Label(root, text='Message: ').pack()

# Add entry (e1 for variable)
e1 = Entry(root)
e1.pack()

# Add button, when clicked pint_entry function will run
Button(root, text="Click Me", command=print_entry).pack()

# Forever loops program (keeps window open) until closed
root.mainloop()