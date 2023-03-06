from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Syntax Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("600x750")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=8, padx=8)

f = Frame(root, bg="grey")

b = Button(f, text="7", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack() //pack button

f = Frame(root, bg="grey")

b = Button(f, text="4", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="1", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="0", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="C", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
b = Button(f, text="=", padx="28", pady="8", font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
