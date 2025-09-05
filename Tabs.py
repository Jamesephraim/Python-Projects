import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry("1100x600")
window.title('Tab in python')


#NoteBook widget
notebook=ttk.Notebook(window)
#Tab 1
tab1=ttk.Frame(notebook,width=400,height=300)
tab1.pack()
label1=ttk.Label(tab1,text='This is Tab 1',font="Lusida 20 bold")
label1.place(x=40,y=30)


#Tab 2

tab2=ttk.Frame(notebook )
entry=ttk.Entry(tab2,font="Arial 20 bold")
entry.pack()
tab2.pack(fill="both",expand=True)

#Tab 3

tab3=ttk.Frame(notebook)

tab3.pack(fill="both",expand=True)

#Tab 4

tab4=ttk.Frame(notebook )

tab4.pack(fill="both",expand=True)

notebook.add(tab1,text="Home",state="normal")

notebook.add(tab2,text="Add")


notebook.add(tab3,text="Edit")

notebook.add(tab4,text="Delete")


notebook.pack(expand=True,pady=30)
notebook.place(x=1,y=1)



window.mainloop()
