import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Functions for contact management

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    
    if not name or not phone:
        messagebox.showerror("Error", "Name and phone number are required.")
        return

    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_entries()
    view_contacts()

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name} - {details['phone']}")

def search_contact():
    search_term = entry_search.get().strip()
    listbox_contacts.delete(0, tk.END)
    
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            listbox_contacts.insert(tk.END, f"{name} - {details['phone']}")

def update_contact():
    name = entry_name.get().strip()
    
    if name in contacts:
        contacts[name]['phone'] = entry_phone.get().strip()
        contacts[name]['email'] = entry_email.get().strip()
        contacts[name]['address'] = entry_address.get().strip()
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", f"Contact '{name}' not found.")

def delete_contact():
    name = entry_name.get().strip()
    
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showerror("Error", f"Contact '{name}' not found.")

def select_contact(event):
    selected_contact = listbox_contacts.get(listbox_contacts.curselection())
    name = selected_contact.split(" - ")[0]
    
    if name in contacts:
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        
        entry_name.insert(0, name)
        entry_phone.insert(0, contacts[name]['phone'])
        entry_email.insert(0, contacts[name]['email'])
        entry_address.insert(0, contacts[name]['address'])

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Contact Management System")

# Input fields for contact details
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_phone = tk.Entry(frame)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_email = tk.Entry(frame)
entry_email.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_address = tk.Entry(frame)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Buttons for adding, updating, deleting, and searching contacts
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Contact", command=add_contact)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_update = tk.Button(button_frame, text="Update Contact", command=update_contact)
btn_update.grid(row=0, column=1, padx=5, pady=5)

btn_delete = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=0, column=2, padx=5, pady=5)

# Search field and button
tk.Label(root, text="Search:").pack(pady=5)
entry_search = tk.Entry(root)
entry_search.pack(pady=5)

btn_search = tk.Button(root, text="Search Contact", command=search_contact)
btn_search.pack(pady=5)

# Listbox to display contacts
listbox_contacts = tk.Listbox(root, width=40, height=10)
listbox_contacts.pack(pady=10)
listbox_contacts.bind('<<ListboxSelect>>', select_contact)

# Display all contacts initially
view_contacts()

# Run the GUI main loop
root.mainloop()
