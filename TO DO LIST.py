from tkinter import *
from tkinter import messagebox

# Function to add tasks
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Task is required")

# Function to delete tasks
def delete_task():
    tasks_selected = tasks_listbox.curselection()
    for task_index in reversed(tasks_selected):
        tasks_listbox.delete(task_index)

# Function to clear all tasks
def clear_all_tasks():
    tasks_listbox.delete(0, END)

# Main Function
def main():
    # Create window
    root = Tk()
    root.title("To Do List")
    root.geometry("350x400")

    # Create labels and entries
    task_label = Label(root, text="Task")
    task_entry = Entry(root, width=30)

    # Create buttons
    add_task_button = Button(root, text="Add Task", command=add_task)
    delete_task_button = Button(root, text="Delete Task", command=delete_task)
    clear_all_tasks_button = Button(root, text="Clear All Tasks", command=clear_all_tasks)

    # Create listbox
    tasks_listbox = Listbox(root, width=50)

    # Position elements in window
    task_label.pack(pady=10)
    task_entry.pack(pady=10)
    add_task_button.pack(pady=10)
    delete_task_button.pack(pady=10)
    clear_all_tasks_button.pack(pady=10)
    tasks_listbox.pack(pady=10)

    # Start main event loop
    root.mainloop()

if __name__ == "__main__":
    main()