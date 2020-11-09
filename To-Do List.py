from tkinter import*
win = Tk()

win.title("To-Do List")

content = Listbox(win, font="Rockwell 24 bold", bg="black", fg="Red")

task = StringVar()
e = Entry(win, textvariable = task, font="Rockwell 24")
add = Button(win, text="Add", font="Ariel 20", padx=10, command = lambda content=content, task=task : content.insert(END,task.get()))
delete = Button(win, text="Delete", font="Ariel 20", command = lambda content=content : content.delete(ANCHOR))


content.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
e.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
add.grid(row=2, column=0, padx=5, pady=20)
delete.grid(row=2, column=1, padx=5, pady=20)


win.mainloop()
