import tkinter as tk
from pytube import YouTube
#global url

 


root=tk.Tk()
root.geometry('900x300')
root.config(bg='skyblue')
root.resizable(False,False)



def download_high():
    #global url
    link=url_entry.get()
    #print(link)
    try:
        print('a')
        object=YouTube(link)
        print('b')

        object=object.streams.get_by_resolution()
        print('c')

        object.download()
        print('d')

        status_high.config(text='Downloaded High Resolution')


    except:
        status_high.config(text='Error')

""" def download_low():
    #global url
    link=url_entry.get()
    #print(link)
    try:
        object=YouTube(link)
        object=object.streams.get_lowest_resolution()
        object.download()
        status_low.config(text='Downloaded Low Resolution')


    except:
        status_low.config(text='Error') """



title=tk.Label(root,text='Video Downloader',bg='red',fg='blue',font='Arial 20 bold ')
title.pack(fill='x')

label=tk.Label(root,text='Enter Valid URL :',font='Arial 19 bold ').place(x=50,y=90)
url_entry=tk.Entry(root,width=43,font='Arial 18 bold ')
url_entry.place(x=280,y=90)

btn=tk.Button(root,text="Download High Resolution",font='Arial 20 bold ',fg='pink',bg='red',command=download_high)
btn.place(x=430,y=140)
""" btn=tk.Button(root,text="Download Low Resolution",font='Arial 20 bold ',fg='pink',bg='red',command=download_low)
btn.place(x=50,y=140) """




#----------------Status----------
status_low=tk.Label(root,font='Arial 20 bold ',text='',bg='skyblue',fg='red')
status_low.place(x=50,y=200)

status_high=tk.Label(root,font='Arial 20 bold ',text='',bg='skyblue',fg='red')
status_high.place(x=430,y=200)

root.mainloop()