from tkinter import *
window = Tk()
window.title("App Evans Meja")


lbl = Label(window, text="Welcome To My Movies App", font=("Arial Bold", 30))
lbl.grid(column=0, row=0)

btn1 = Button(window, text="Button1", bg="orange", fg="red")
btn1.grid(column=0, row=1)

btn2 = Button(window, text="Button2", bg="purple", fg="green")
btn2.grid(column=1, row=1)

btn3 = Button(window, text="Button3", bg="white", fg="blue")
btn3.grid(column=2, row=1)

def clicked():
    lbl.configure(text="Button was clicked !!")

window.geometry('850x800')
window.mainloop()