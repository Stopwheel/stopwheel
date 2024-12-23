import tkinter as tk

root = tk.Tk()
root.title("計算機")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
Button = ['1', '2', '3', '/', '4', '5', '6', '*', '7', '8', '9', '-', 'c', '0', '=', '+']
for i, Button in enumerate(Button):
    btn = tk.Button(root, text=Button, font=('Arial', 20), command=lambda b=Button: on_click(b))
    btn.grid(row=(i // 4) + 1, column=i % 4, sticky="nsew")
    root.columnconfigure(i % 4, weight=1)
def on_click(btn_txt):
    value_txt = entry_var.get()
    if btn_txt == "=":
        try:
            result = eval(value_txt)
            entry_var.set(result)
        except Exception:
            entry_var.set('error')
    elif btn_txt.lower() == "c":  
        entry_var.set("")
    else:
        entry_var.set(value_txt + btn_txt)

root.mainloop()