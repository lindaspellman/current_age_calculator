import tkinter as tk

# Create a new instance of Tkinter
root = tk.Tk()

# Set the title of the window
root.title("Single Window")

# Create a label widget
label = tk.Label(root, text="Hello, world!")

# Pack the label into the window
label.pack()

# Run the Tkinter event loop
root.mainloop()