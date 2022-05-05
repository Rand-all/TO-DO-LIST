from tkinter import *   #imports everything from tkinter module
from tkinter import messagebox  #imports message box  #add task #delete task


#function to enter new task
def newTask():    
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

#function to delete task
def deleteTask():
    lb.delete(ANCHOR)


#window initializes Tk() as the main window
window = Tk()
window.geometry('500x450+500+200')
window.title('Task Today')
window.config(bg='#223441')
window.resizable(width=False, height=False)

#used to hold other widgets
frame = Frame(window)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    window,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='yellow',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='purple',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

window.mainloop()

