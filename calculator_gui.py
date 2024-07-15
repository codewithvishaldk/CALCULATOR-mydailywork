import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Set up the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Entry widget for the calculator
entry = tk.Entry(app, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
entry.pack(pady=20)

# Buttons layout
button_frame = tk.Frame(app)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 0
col_val = 0

for button in buttons:
    if button == 'C':
        btn = tk.Button(button_frame, text=button, width=5, height=2, command=clear)
    elif button == '=':
        btn = tk.Button(button_frame, text=button, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(button_frame, text=button, width=5, height=2, command=lambda b=button: click(b))
    
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
