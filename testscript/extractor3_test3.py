# IMPORTS:

import tkinter as tk
from tkinter import filedialog as tk_fd
from tkinter import ttk as ttk
from PIL import Image,ImageTk

# GLOBAL VARIABLES:



# METHODS

def load_image(filepath=None):
    #img=Image.open(filepath)
    #img=Image.open(f"testimages/sine.png")
    #resized_image= img.resize((500,500), Image.Resampling.LANCZOS)
    #tk_img = ImageTk.PhotoImage(resized_image)
    #image_container = gui_center_canvas.create_image(10,10, anchor="nw",image=tk_img)
    #gui_center_label_img.configure(image=tk_img)

    if filepath == None:
        print("no file selected, creating blank image")
        img = Image.new('RGB', (500, 500)) # create blank image when no filepath suplied
        img_resized = img
    else:
        print(f"loading file {filepath}")
        img=Image.open(filepath) # load file when path is specified
        print(f"resizing file {filepath}")
        img_resized = img.resize((500,500), Image.Resampling.LANCZOS) # create resized copy of image 

    img_tk = ImageTk.PhotoImage(img_resized) # create tk image object for gui
    gui_center_label_img.configure(image=img_tk) # update center image view
    gui_center_label_img.img_tk = img_tk



# METHODS: BUTTONS

def btn_select_file():
    print("pls select a file you want to load")
    filepath = tk_fd.askopenfilename()
    print(f'setting file input entry to {filepath}')
    #var_filepath_selected.set(filepath)
    gui_controlls_entry_filepath.delete(0, "end")
    gui_controlls_entry_filepath.insert(0, filepath)


def btn_load_file():
    filepath = gui_controlls_entry_filepath.get()
    print(f'trying to load file: {filepath}')
    load_image(filepath=filepath)
    #img=Image.open(f"testimages/sine.png")
    #resized_image= img.resize((500,500), Image.Resampling.LANCZOS)
    #img2= ImageTk.PhotoImage(resized_image)
    

    
    #image_container = gui_center_canvas.create_image(10,10, anchor="nw",image=img2)
    #gui_center_canvas.itemconfig(image_container ,image=img)
    #load_image(filepath=filepath) # trying to load the selected file
    #gui_center_canvas.grid(column=0, row=1, sticky=tk.N+tk.S+tk.W)


def btn_clear():
    #print("clearing canvas")
    #gui_center_canvas.delete("all")
    pass

# GUI

gui_window = tk.Tk() # create window instacne
gui_window.geometry("1400x600") # set geometry of the window
gui_window.title('FigureSample') # set name of window


# configure layout of grid : columns
gui_window.columnconfigure(0, weight=0)
gui_window.columnconfigure(1, weight=3)
gui_window.columnconfigure(2, weight=3)

# configure layout of grid : rows
gui_window.rowconfigure(0, weight=3)
gui_window.rowconfigure(0, weight=3)
gui_window.rowconfigure(0, weight=3)


# FRAMES:
gui_frame_controlls = tk.Frame(master=gui_window, bg="gray", width=500, height=500) # create controll frame
gui_frame_center = tk.Frame(master=gui_window, bg="red", width=100, height=100) # create frame for the image currently worked on
gui_frame_evaluation = tk.Frame(master=gui_window, bg="blue", width=100, height=100) # create frame for the captured results

# FRAMES: layout
gui_frame_controlls.grid(column=0, row=0,sticky=tk.N+tk.S)#, sticky=tk.E+tk.W) #.pack(side = tk.LEFT, expand=False) # but controlls on the left
gui_frame_center.grid(column=1, row=0, sticky=tk.E+tk.W+tk.N+tk.S) #.pack(side = tk.LEFT, fill=tk.BOTH) # but controlls on the left
gui_frame_evaluation.grid(column=2, row=0, sticky=tk.E+tk.W+tk.N+tk.S)#.pack(side = tk.RIGHT, fill=tk.BOTH) # but controlls on the left



# FRAME: CONTROLLS
# controll frame: widgets
gui_label_1 = tk.Label(gui_frame_controlls, text="Cotrolls, Settings & Configuration", bg="gray", fg="white")
gui_controlls_button_selectfile = tk.Button(gui_frame_controlls, text="Select File", command=btn_select_file)
gui_controlls_button_loadfile = tk.Button(gui_frame_controlls, text="Load Selected File", command=btn_load_file)
gui_controlls_button_clear = tk.Button(gui_frame_controlls, text="Clear", command=btn_clear)
gui_controlls_entry_filepath = tk.Entry(gui_frame_controlls, width=50)
#gui_controlls_separator_1 = ttk.Separator(gui_frame_controlls, orient='horizontal')

# controll frame: widgets layout
gui_label_1.grid(column=0, row=0,sticky=tk.N+tk.S)
#gui_controlls_separator_1.grid(column=0, row=1,sticky=tk.W+tk.E)
gui_controlls_entry_filepath.grid(column=0, row=1, columnspan=2, sticky=tk.W+tk.E)
gui_controlls_button_selectfile.grid(column=0, row=2, sticky=tk.W+tk.E)
gui_controlls_button_loadfile.grid(column=1, row=2, sticky=tk.W+tk.E)
gui_controlls_button_clear.grid(column=2, row=2, sticky=tk.W+tk.E)


# FRAME: CENTER
# center frame: widgets
gui_label_2 = tk.Label(gui_frame_center, text="Working Image", bg="orange", fg="white")
#gui_center_canvas = tk.Canvas(gui_frame_center, height=500, width=500)
gui_center_label_img = tk.Label(gui_frame_center, text="img", bg="black", fg="white")


# center frame: widgets layout
gui_label_2.grid(column=0, row=0,sticky=tk.N+tk.S+tk.W)
#gui_center_canvas.grid(column=0, row=1, sticky=tk.N+tk.S+tk.W)
gui_center_label_img.grid(column=0, row=1, sticky=tk.N+tk.S+tk.W)


# FRAME EVALUATION
# evaluation frame: widgest
gui_label_3 = tk.Label(gui_frame_evaluation, text="Results", bg="green", fg="white")

# evaluation frame: widgets layout
gui_label_3.grid(column=0, row=0,sticky=tk.N+tk.S)


#load_image(filepath=None)
#load_image("testimages/sine.png")

load_image()



gui_window.mainloop() # run window
