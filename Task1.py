import tkinter
import tkinter.messagebox
import pickle
root = tkinter.Tk()
root.title("To Do list")
def add_task():
    task = entry_task.get()
    if task != "":
        Listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")
def delete_task():
    try:
        task_index = Listbox_task.curselection()[0]
        Listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def load_task():
    try:
        task = pickle.load(open("task.dat", "rb"))
        Listbox_task.delete(0, tkinter.END)
        for task in task:
            Listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="cannnot find task.dat.")


def save_task():
    task = Listbox_task.get(0, Listbox_task.size())
    pickle.dump(task, open("task.dat", "wb"))


#create GUI
frame_task = tkinter.Frame(root)
frame_task.pack()

Listbox_task = tkinter.Listbox(frame_task, height=10, width=50)
Listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

Listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=Listbox_task.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button = tkinter.Button(root, text="Add task", width=48, command=add_task)
button.pack()

button = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button.pack()

button = tkinter.Button(root, text="Load task", width=48, command=load_task)
button.pack()

button = tkinter.Button(root, text="Save task", width=48, command=save_task)
button.pack()


root.mainloop()