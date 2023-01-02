# INI CALCULATOR BAGUS NEW VERSION
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Set the weight of the rows and columns in the grid
for i in range(5):
    window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(i, weight=1)

# Create the display and set its starting value
display = tk.Entry(window, width=35, font=("Helvetica", 16))
display.grid(row=0, column=0, columnspan=5, sticky="nsew")
display.insert(0, "0")

# Define the calculator's buttons
buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "("],
    ["1", "2", "3", "-", ")"],
    ["0", ".", "=", "+"]
]

# Create the buttons and add them to the window
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        font_size = int(0.5*(window.winfo_width()+window.winfo_height())/len(row))
        tk.Button(window, text=button, width=5, font=("Helvetica", font_size), command=lambda x=button: press(x)).grid(row=i+1, column=j, sticky="nsew")

# Define the behavior of the buttons
def press(key):
    # If the key is "C", clear the display
    if key == "C":
        display.delete(0, tk.END)
        display.insert(0, "0")
        return
    
    # If the key is "=", evaluate the expression and display the result
    if key == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(0, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
        return
    
    # Otherwise, add the key to the display
    current = display.get()
    if current == "0":
        display.delete(0, tk.END)
    display.insert(tk.END, key)

# Run the main loop
window.mainloop()
