import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(bg="red", height=100, width=100)
canvas.pack(anchor=tk.NW)

button = tk.Button(text="button")
button.pack(side=tk.RIGHT, anchor=tk.SE)

root.mainloop()