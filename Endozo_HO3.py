import tkinter as azl

window = azl.Tk()
window.title("Cute")
window.configure(bg="lightblue")

label = azl.Label(window, text="Simple Calculator",font=("times new roman", 15, "bold"),bg="lightblue", fg="darkblue")
label.grid(column=0, row=0, padx=50, pady=10, columnspan=3)

def rss():
    a = int(first_entry.get())
    b = int(sec_entry.get())
    result = a + b
    label = azl.Label(window, text=f"The sum of {a} and {b} is {result}.", font=("times new roman", 15, "bold"),bg="lightblue", fg="darkblue")
    label.grid(column=0, row=5, columnspan=3)

def ndz():
    a = int(first_entry.get())
    b = int(sec_entry.get())
    dif = a - b
    label = azl.Label(window, text=f"The difference of {a} and {b} is {dif}.",font=("times new roman", 15, "bold"),bg="lightblue", fg="darkblue")
    label.grid(column=0, row=5, columnspan=3)

def angl():
    a = int(first_entry.get())
    b = int(sec_entry.get())
    prod = a * b
    label = azl.Label(window, text=f"The product of {a} and {b} is {prod}.",font=("times new roman", 15, "bold"), bg="lightblue", fg="darkblue")
    label.grid(column=0, row=5, columnspan=3)

def taray():
    a = int(first_entry.get())
    b = int(sec_entry.get())
    quot = a / b
    label = azl.Label(window, text=f"The quotient of {a} and {b} is {quot}.",font=("times new roman", 15, "bold"),bg="lightblue", fg="darkblue")
    label.grid(column=0, row=5, columnspan=3)

first = azl.Label(window, text="Enter a number:",font=("times new roman", 15), bg="lightblue")
first.grid(column=0, row=1)

first_entry = azl.Entry(window, width=20)
first_entry.grid(column=1, row=1, columnspan=2)

sec = azl.Label(window, text="Enter a number:",font=("times new roman", 15), bg="lightblue")
sec.grid(column=0, row=2)
sec_entry = azl.Entry(window, width=20)
sec_entry.grid(column=1, row=2, columnspan=2)

add_btn = azl.Button(window, text="ADD", width=10, bg="#aec6a5", command=rss)
add_btn.grid(column=0, row=3, pady=10)

sub_btn = azl.Button(window, text="SUBTRACT", width=10, bg="#aec6a5", command=ndz)
sub_btn.grid(column=1, row=3, pady=10)

mul_btn = azl.Button(window, text="MULTIPLY", width=10, bg="#aec6a5", command=angl)
mul_btn.grid(column=0, row=4, pady=10)

div_btn = azl.Button(window, text="DIVIDE", width=10, bg="#aec6a5", command=taray)
div_btn.grid(column=1, row=4, pady=10)

window.mainloop()