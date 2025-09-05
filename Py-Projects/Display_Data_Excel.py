import tkinter as tk
from tkinter import ttk
import openpyxl


def load_data():
    #my Excel filepath
    filepath=r"C:\Users\admin\Desktop\Python\data.xlsx"
    #load or open my workbook
    workbook=openpyxl.load_workbook(filepath)
    # select sheet in my workbook
    sheet=workbook.active
    #All data can store 
    list_values=list(sheet.values)
        #print(list_values)
    #collect Headings
    cols=list_values[0]
    #print(cols)

    #Creating a excel design
    tree=ttk.Treeview(root,column=cols,show="headings")

    #Display HEadings
    for col_name in cols:
        tree.heading(col_name,text=col_name)
        
    tree.pack(expand=True,fill='y')


    #getting all values / records
    for values in list_values[1:]:
        #insert the data
        tree.insert('',tk.END,values=values)


    








root=tk.Tk()
root.title("Dispaly Data in Excel File")









load_data()



root.mainloop()








 
