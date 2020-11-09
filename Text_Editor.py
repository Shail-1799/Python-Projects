from tkinter import*
from tkinter import filedialog
def openfile():

    try:
        t = filedialog.askopenfile(mode="r", title="Select File", filetypes = [("All Files","*.*")])
        Content.insert(END, t.read())
    except:
        print("Could not open the file !")
    finally:
        if t:
            t.close()

def savefile():

    f=filedialog.asksaveasfile(mode="w", defaultextension=".txt")

    if f is None:
        return
    try:
        usertext=str(Content.get(1.0,END))
        f.write(usertext)
    except:
        print("Could not save the file !")
    finally:
        f.close()

def closewin():
    win.destroy()


win = Tk()

Mainmenu = Menu(win)
win.config(menu = Mainmenu)

Filemenu = Menu(Mainmenu)
Mainmenu.add_cascade(label="File", menu = Filemenu)

Filemenu.add_command(label="Open", command=openfile)
Filemenu.add_command(label="Save", command=savefile)
Filemenu.add_separator()
Filemenu.add_command(label="Close", command=closewin)

#Mainmenu.add_command(label="Help")

Content= Text(win, width=100)
Content.grid(row=0, column=0, padx=10, pady=10)



win.mainloop()