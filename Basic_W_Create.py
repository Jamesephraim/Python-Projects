import tkinter  as tk
import tkinter.colorchooser as tk_color


root=tk.Tk()

root.geometry('400x400')
root.config(bg='skyblue')
root.title('Create New Window')


window_info={'file_name':'No-Name.py','color':''}
#---------------------------------------------


def set_color():
    if 'custom' in color.get():
        selected_color=(tk_color.askcolor()[1])

        if selected_color:
            window_info['color']=selected_color
        else:
            window_info['color']=''
            color.set('defualt')

    else:
        window_info['color']='black'

        
def set_file_name():
    if str(f_name.get()).endswith('.py'):
        window_info['file_name']=f_name.get()
    else:
        window_info['file_name']=str(f_name.get()) + '.py'


def build():
    set_file_name()
    setup_geometry=f"root.geometry('{f_width.get()}x{f_height.get()}')"
    setup_color=f''
    setup_title=f''
    setup_heading=f''


    if f_heading.get() and f_heading_bg.get():
        setup_heading=f"tk.Label(root,text='{f_heading.get()}',bg='{f_heading_bg.get()}').pack(fill=tk.X)"

    if f_title.get():

        setup_title=f"root.title(\'{f_title.get()}\')"



    if color.get() != 'default':
        setup_color=f"root.config(bg=\'{window_info['color']}\')"

    if setup_geometry and setup_color and setup_heading and setup_title :
   
        with open(window_info['file_name'],'w') as write_file:
            write_file.write(f"""

import tkinter as tk
                            
root=tk.Tk()
{setup_geometry}
{setup_color}
{setup_title}
{setup_heading}

root.mainloop()


"""                            )
            write_file.close()



#--------------------------------------------



tk.Label(root,text='Create New Window',bg='orange',fg='blue',font='Arial 15').pack(fill=tk.X)

tk.Label(root,text='Select File Name :',font='Arial 15',bg='skyblue').place(x=20,y=30)
f_name=tk.Entry(root)
f_name.place(x=200,y=30)

tk.Label(root,text='Select Title :',font='Arial 15',bg='skyblue').place(x=20,y=80)
f_title=tk.Entry(root)
f_title.place(x=200,y=80)


color=tk.StringVar()
color.set('d_color')
d_color=tk.Radiobutton(root,text='Default Color',font='Arial 15',bg='skyblue',variable=color,value='defualt',command=set_color)
d_color.place(x=10,y=130)

r_color=tk.Radiobutton(root,text='Select Color',font='Arial 15',bg='skyblue',variable=color,value='custom',command=set_color)
r_color.place(x=200,y=130)


tk.Label(root,text='Set Width :',font='Arial 15',bg='skyblue').place(x=20,y=180)
f_width=tk.Spinbox(root,from_=30,to=100000)
f_width.place(x=200,y=180)


tk.Label(root,text='Set Height :',font='Arial 15',bg='skyblue').place(x=20,y=210)
f_height=tk.Spinbox(root,from_=30,to=100000)
f_height.place(x=200,y=210)

tk.Label(root,text='Enter Heading :',font='Arial 15',bg='skyblue').place(x=20,y=260)
f_heading=tk.Entry(root)
f_heading.place(x=200,y=260)

tk.Label(root,text='Heading BG :',font='Arial 15',bg='skyblue').place(x=20,y=300)
f_heading_bg=tk.Entry(root)
f_heading_bg.place(x=200,y=300)


btn=tk.Button(root,text='BUILD WINDOW',font='Arial 18',bg='red',command=build)
btn.place(x=110,y=350)





root.mainloop()