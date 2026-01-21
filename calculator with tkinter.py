import tkinter as tk

def on_click(button_value):
    current = entry_var.get()
    if button_value == '=':
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == 'C':
        entry_var.set('')
    else:
        entry_var.set(current + button_value)


root = tk.Tk()
root.title("Calculator")
root.configure(bg='#B287A3')  


entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 18), bg='#ffffff')  
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Label for your name
your_name_label = tk.Label(root, text="Pankaj's calculator", font=('Ink Free', 12), bg='#99ccff') 
your_name_label.grid(row=7, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: on_click(b), bg='#b3d9ff').grid(row=row_val, column=col_val)  # Set the background color to a lighter blue
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main loop
root.mainloop()


