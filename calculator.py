import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=40, pady=20, command=lambda text=text: button_click(text))
    button.grid(row=row, column=col)


clear_button = tk.Button(root, text="Clear", padx=81, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)


calc_button = tk.Button(root, text="Calculate", padx=80, pady=20, command=calculate)
calc_button.grid(row=5, column=2, columnspan=2)

root.mainloop()
