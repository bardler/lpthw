import Tkinter as Tk
import tkMessageBox

top = Tk.Tk()

# different functions for dialog boxes
def info():
    tkMessageBox.showinfo("info box", "info message")

def warning():
    tkMessageBox.showwarning("warning box", "warning message")

def error():
    tkMessageBox.showerror("error box", "error message")

def question():
    tkMessageBox.askquestion("question box", "question? message")

def okcancel():
    tkMessageBox.askokcancel("ok box", "ok message")

def yesno():
    tkMessageBox.askyesno("yes no box", "yes no message")

def retrycancel():
    tkMessageBox.askretrycancel("retry cancel box", "retry message")

#setup
B1 = Tk.Button(top, text="info button", command=info)
B1.pack()

B2 = Tk.Button(top, text="warning button", command=warning)
B2.pack()

B3 = Tk.Button(top, text="error button", command=error)
B3.pack()

B4 = Tk.Button(top, text="question button", command=question)
B4.pack()

B5 = Tk.Button(top, text="ok cancel button", command=okcancel)
B5.pack()

B6 = Tk.Button(top, text="yes no button", command=yesno)
B6.pack()

B7 = Tk.Button(top, text="retry cancel button", command=retrycancel)
B7.pack()

# other widets from here http://www.tutorialspoint.com/python/python_gui_programming.htm
B8 = Tk.Canvas(top, bg="blue", height=50, width=50)
B8.pack()

B9 = Tk.Checkbutton(top, text="This is a Checkbox",)
B9.pack()

B10 = Tk.Entry(top, text="Entry Box")
B10.pack()

B11 = Tk.Button(top, text="Red", fg="red")
B11.pack()

B12 = Tk.StringVar()
B12_label = Tk.Label(top, textvariable=B12, relief=Tk.RAISED)
B12.set("This is a text line")
B12_label.pack()

B13 = Tk.Listbox(top)
B13.insert(1, "Option 1")
B13.insert(2, "Option 2")
B13.insert(3, "Option 3")
B13.pack()

#Menu button
B14 = Tk.Menubutton(top, text="Menu", relief=Tk.RAISED)
B14.grid()
B14.menu=Tk.Menu(B14, tearoff=0)
B14["menu"]=B14.menu

opt1 = Tk.IntVar()
opt2 = Tk.IntVar()

B14.menu.add_checkbutton(label="Option 1", variable=opt1)
B14.menu.add_checkbutton(label="Option 2", variable=opt2)

B14.pack()

#Menu. ie file, edit, help.
def temp_button():
    file_win = Tk.Toplevel(top)
    button = Tk.Button(file_win, text="temp button")
    button.pack()

def help_about():
    file_win = Tk.Toplevel(top)
    print "This is a test" #prints to console
    button = Tk.StringVar
    button_label = Tk.Label(file_win, textvariable=button, relief=Tk.RAISED)
    button.set("This is a test file")
    button_label.pack()


menu_bar=Tk.Menu(top)

    #file menu
file_menu = Tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=temp_button)
file_menu.add_command(label="Open", command=temp_button)
file_menu.add_command(label="Save", command=temp_button)
file_menu.add_command(label="Save as...", command=temp_button)
file_menu.add_command(label="Close", command=temp_button)
#seperator
file_menu.add_separator()
file_menu.add_command(label="Exit", command=top.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

    #edit menu
edit_menu = Tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="undo", command=temp_button)
#seperator
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=temp_button)
edit_menu.add_command(label="Copy", command=temp_button)
edit_menu.add_command(label="Paste", command=temp_button)
edit_menu.add_command(label="Delete", command=temp_button)
edit_menu.add_command(label="Select All", command=temp_button)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

    #help menu
help_menu = Tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", command=temp_button)
help_menu.add_command(label="About...", command=help_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

    #menu config
top.config(menu=menu_bar)

#run loop
top.mainloop()


