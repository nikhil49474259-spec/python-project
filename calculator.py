from tkinter import *

root = Tk()
root.title("My Calculator")
root.geometry("400x500")

# Calculator screen
screen = Entry(root, font="Arial 24", justify="right", bd=20)
screen.grid(row=0, column=0, columnspan=4, sticky="nsew")

def click(value):
	screen.insert(END, value)
       
def clear():
	screen.delete(0,END)
	
def calculate():
	try:
		result = eval(screen.get())
		screen.delete(0,END)
		screen.insert(0,result)
	except:
		screen.delete(0,END)
		screen.insert(0,"Error")

btn7 = Button(root, text="7", font="Arial 18", command=lambda: click("7"))
btn7.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

btn8 = Button(root, text="8", font="Arial 18", command=lambda: click("8"))
btn8.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

btn9 = Button(root, text="9", font="Arial 18", command=lambda: click("9"))
btn9.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

btn_div = Button(root, text="/", font="Arial 18", command=lambda: click("/"))
btn_div.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

btn4 = Button(root, text="4", font="Arial 18", command=lambda: click("4"))
btn4.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

btn5 = Button(root, text="5", font="Arial 18", command=lambda: click("5"))
btn5.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

btn6 = Button(root, text="6", font="Arial 18", command=lambda: click("6"))
btn6.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

btn_mul = Button(root, text="*", font="Arial 18", command=lambda: click("*"))
btn_mul.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

btn1 = Button(root, text="1", font="Arial 18", command=lambda: click("1"))
btn1.grid(row=3, column =0, sticky="nsew", padx=2, pady=2)

btn2 = Button(root, text="2", font="Arial 18", command=lambda: click("2"))
btn2.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

btn3 = Button(root, text="3", font="Arial 18", command=lambda: click("3"))
btn3.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

btn_sub = Button(root, text="-", font="Arial 18", command=lambda: click("-"))
btn_sub.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

btn0 = Button(root, text="0", font="Arial 18", command=lambda: click("0"))
btn0.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

btn_dot = Button(root, text=".", font="Arial 18", command=lambda: click("."))
btn_dot.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)

btn_eq = Button(root, text="=", font="Arial 18", command=lambda: calculate())
btn_eq.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

btn_add = Button(root, text="+", font="Arial 18", command=lambda: click("+"))
btn_add.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

btn_c = Button(root, text="c", font="Arial 18", bg="red", fg="white", command=clear)
btn_c.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)



root.mainloop()
0

print ("thanks for using")

0
