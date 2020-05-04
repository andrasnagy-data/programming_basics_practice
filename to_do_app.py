import tkinter as tk

# tkinter object
root = tk.Tk()

# screen title
root.title("Be productive.")
root.geometry("700x700")

# task lists
tasks_list = []

# functions
# get task and append to list
def task_list():
    task = str(tasks.get())
    tasks_list.append((task))
    return tasks_list

# display task
def task_display():
    show_task = task_list()

    # creating text field
    show_task_display = tk.Text(master= root, height= 15, width= 40)
    show_task_display.grid(column= 2, row= 3)
    # printing onto text field
    show_task_display.insert(tk.END, show_task)
    # deleting entry text
    tasks.delete(first= 0, last= 30)

# labels
welcome_label = tk.Label(text= "Write a to do list with this small app.")
welcome_label.grid(column= 0, row= 0)

to_do_label = tk.Label(text= "To do today")
to_do_label.grid(column= 0, row= 2)

# entries
tasks = tk.Entry()
tasks.grid(column= 1, row= 2)

# button
button1 = tk.Button(text= "Proceed", command= task_display)
button1.grid(column= 1, row= 3)

# run app
root.mainloop()
