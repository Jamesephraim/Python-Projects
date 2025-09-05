import tkinter 
from tkinter import *




root=Tk()

root.title("Number converter")
root.geometry('300x400')
root.configure(bg="Yellow")


dec=0



def dec_bin():
    dec_label=Label(root,text="Enter Dec Number :")
    dec_label.place(x=20,y=30)
    dec=Entry(root)
    dec.place(x=130,y=30)
    
    

     
    
    bin_label=Label(root,text="Binary :")
    bin_label.place(x=20,y=70)
    bin_val=Label(root,bg='white',fg='blue',width=17)
    bin_val.place(x=130,y=70)

    oct_label=Label(root,text="Octal :")
    oct_label.place(x=20,y=110)
    oct_val=Label(root,bg='white',fg='blue',width=17)
    oct_val.place(x=130,y=110)

    hex_label=Label(root,text="HexaDecimal :")
    hex_label.place(x=20,y=150)
    hex_val=Label(root,bg='white',fg='blue',width=17)
    hex_val.place(x=130,y=150)

    btn=Button(root,text="Convert",width=10,bg='blue',fg='white')
    btn.place(x=150,y=190)


    a=bin(dec)
#def decimal():
    bin_val["text"]=a 
    
    

menu=Menu(root)


type_menu=Menu(menu,tearoff=False)
 
menu.add_cascade(label="Base Converter",menu=type_menu)
type_menu.add_command(label="Dec - Bin",command=dec_bin)
type_menu.add_command(label="Dec - Oct",command=lambda: print('Hello '))
type_menu.add_command(label="Dec - Hex",command=lambda: print('Hello '))
type_menu.add_command(label="Bin - Dec",command=lambda: print('Hello '))
type_menu.add_command(label="Bin - Oct",command=lambda: print('Hello '))
type_menu.add_command(label="Bin - Hex",command=lambda: print('Hello '))
type_menu.add_command(label="Oct - Dec",command=lambda: print('Hello '))
type_menu.add_command(label="Oct - Bin",command=lambda: print('Hello '))
type_menu.add_command(label="Oct - Hex",command=lambda: print('Hello '))
type_menu.add_command(label="Hex - Dec",command=lambda: print('Hello '))
type_menu.add_command(label="Hex - Bin",command=lambda: print('Hello '))
type_menu.add_command(label="Hex - Oct",command=lambda: print('Hello '))

root.configure(menu=menu)

 


root.mainloop()
