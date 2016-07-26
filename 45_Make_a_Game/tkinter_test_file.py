import Tkinter
# or use import Tkinter as TK, to shorten call TK.Button for example
import tkMessageBox

top = Tkinter.Tk()

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
B1 = Tkinter.Button(top, text = "info button", command = info)
B1.pack()

B2 = Tkinter.Button(top, text = "warning button", command = warning)
B2.pack()

B3 = Tkinter.Button(top, text = "error button", command = error)
B3.pack()

B4 = Tkinter.Button(top, text = "question button", command = question)
B4.pack()

B5 = Tkinter.Button(top, text = "ok cancel button", command = okcancel)
B5.pack()

B6 = Tkinter.Button(top, text = "yes no button", command = yesno)
B6.pack()

B7 = Tkinter.Button(top, text = "retry cancel button", command = retrycancel)
B7.pack()

# other widets
B8 = Tkinter.Canvas(top, bg="blue", height=50, width=50)
B8.pack()

B9 = Tkinter.Checkbutton(top, text = "This is a Checkbox",)
B9.pack()

B10 = Tkinter.Entry(top, text = "Entry Box")
B10.pack()

redbutton = Tkinter.Button(top, text="Red", fg="red")
redbutton.pack( side = Tkinter.BOTTOM)

#run loop
top.mainloop()


