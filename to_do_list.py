import tkinter as tk
from tkinter import messagebox
import json

TASKS_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Update the listbox with tasks
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_text = f"{task['title']} - {'Done' if task['completed'] else 'Pending'}"
        task_listbox.insert(tk.END, task_text)

# Add a new task
def add_task():
    title = task_entry.get()
    if not title:
        messagebox.showwarning("Warning", "Please enter a task title.")
        return
    
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    task_entry.delete(0, tk.END)
    update_task_listbox()

# Mark selected task as completed
def mark_task_completed():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")
        return
    
    task_index = selected_task_index[0]
    tasks[task_index]["completed"] = True
    save_tasks(tasks)
    update_task_listbox()

# Delete selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if not selected_task_index:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return
    
    task_index = selected_task_index[0]
    tasks.pop(task_index)
    save_tasks(tasks)
    update_task_listbox()

root = tk.Tk()
root.title("To-Do List")

# Load tasks from file
tasks = load_tasks()

# Task entry and add button
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Task listbox
task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)
update_task_listbox()

# Mark completed and delete buttons
mark_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Start the application
root.mainloop()
