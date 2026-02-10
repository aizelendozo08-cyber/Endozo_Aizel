import tkinter as tk  

window = tk.Tk()
window.title("My Profile")
window.geometry("600x600")
window.resizable(False, True)


title_label = tk.Label(
    window, 
    text='My Profile', 
    font=('Arial', 30, 'bold'),  
    fg="pink",  
    bg='black', 
    anchor='center'
)
title_label.pack(padx=10, pady=10)


tk.Label(window, text="Aizel Ross Endozo", font=('Arial', 20), anchor="w").pack(fill="x", padx=20, pady=5)
tk.Label(window, text="18", font=('Arial', 20), anchor="w").pack(fill="x", padx=20, pady=5)
tk.Label(window, text="BSIT_1A", font=('Arial', 20), anchor="w").pack(fill="x", padx=20, pady=5)
tk.Label(window, text="August 6, 2007", font=('Arial', 20), anchor="w").pack(fill="x", padx=20, pady=5)
tk.Label(window, text="Do your best and God will do the rest", font=('Arial', 20), anchor="w").pack(fill="x", padx=20, pady=5)


window.mainloop()
