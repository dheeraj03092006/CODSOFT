import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get the numbers entered by the user
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Get the selected operation
        operation = operation_var.get()
        
        # Perform the calculation based on the chosen operation
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is undefined.")
                return
            result = num1 / num2
        elif operation == "Modulus":
            result = num1 % num2
        else:
            result = "Invalid operation"
        
        # Display the result
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create labels, entry boxes, and buttons
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Dropdown menu for selecting an operation
operation_var = tk.StringVar(value="Addition")
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Modulus")
operation_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI main loop
root.mainloop()
