import tkinter as tk
from tkinter import *
import socket
import os
import numpy
import cv2
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox

IP='127.0.0.1'
PORT=1117
bg_sub_window='skyblue'






def send_file():
    
    #global filepath
    
    send_file_window=tk.Toplevel()
    send_file_window.title('Send Files')
    send_file_window.geometry('600x500')
    send_file_window.config(bg=bg_sub_window)

    def select():
        global filepath
        filepath=filedialog.askopenfilename(title='Open File',filetypes=[('TextFiles','.txt'),('Python','.py'),('Excel','.xlsx')])
        send_file_window.title(f'Shareing File - {filepath}')
        #return filepath

    def send_data():
        #global filepath
        I=socket.gethostname()
        P=port.get()
        #print(I,P)
        
        if (not str(P)):
            messagebox.showerror(title='Error !!',message=' Please Enter Port !!')
        elif  (str(P) < str(1024))  :
            messagebox.showerror(title='Error !!',message='Port Mustbe Above(1024)')

        elif (str(P) > str(65535)):
            messagebox.showerror(title='Error !!',message='Port Mustbe Below(65535) ')

        elif  (filepath == ""):
            messagebox.showerror(title='Error !!',message='Select Any file')




        elif str(I) and str(P):
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# ipv4 and tcp
            s.bind((str(I),int(P)))
            s.listen(1)
            #print('Listening ............')
            #print('Connection ---'+I,P,filepath)
            conn,addr=s.accept()
            messagebox.showinfo(title='User',message=f'Connection From {addr}')
            #status_file['text']=f'{addr}'
            #Send File path
            #conn.send(str(filepath),'utf-8')
            file=open(filepath,'r')
            data=file.read()
            conn.send(bytes(data,'utf-8'))
            file.close()
            s.close()
            messagebox.showinfo(title='Status',message='Sucessfully File Sended')

 
    heading=tk.Label(send_file_window,text='Sending Files',bg='orange',fg='blue',font='Arial 20 bold')
    heading.pack(fill='x')

    

    
    

    tk.Label(send_file_window,text='Your Device :',bg=bg_sub_window).place(x=80,y=150)
    ip=tk.Label(send_file_window,text=f'{socket.gethostname()}',bg='blue',fg='white',font='bold 15')
    ip.place(x=180,y=150) 

    tk.Label(send_file_window,text='Set PORT :',bg=bg_sub_window).place(x=80,y=200)
    port=tk.Spinbox(send_file_window,from_=1024,to=65535)
    port.place(x=180,y=200) 


    select_btn=tk.Button(send_file_window,text=' + Select File',bg='green',fg='white',font='Arial 15',command=select)
    select_btn.place(x=370,y=80)

    send_btn=tk.Button(send_file_window,text='Send',bg='red',fg='gray',font='Arial 15',command=send_data)
    send_btn.place(x=250,y=360)


    #status_file=tk.Label(send_file_window,text='No Devices').place(x=300,y=300)

    send_file_window.mainloop()
    send_file_window.destroy()


def receive_file():

    
    fname=''
    receive_file_window=tk.Toplevel()
    receive_file_window.title('Receving Files')
    receive_file_window.geometry('400x400')
    receive_file_window.config(bg=bg_sub_window)
    """ ip='hello'
    port=0

    f_name='hi' """

    def file_fun():
        
        I=ip.get()
        P=port.get()
        if (not str(I)):
            messagebox.showerror(title='Error !!',message='Device ID is Empty !!')

        elif (not str(P)):
            messagebox.showerror(title='Error !!',message='Please Enter Port  !!')


        elif (str(P) < str(1024)) and (str(P) > str(65535)):
            messagebox.showerror(title='Error !!',message='Port Below(65535) Above(1024)')

        elif str(I) and str(P):
        
            c=socket.socket()
            c.connect((str(I),int(P)))
            #path='/home/ubentu/Desktop/My Project/Chat/'+fname
            file=open(fname,'w')
            file.write(c.recv(1024).decode())
            #print(data)
            file.close()
            messagebox.showinfo(title='',message=f'File Saved - {fname}')
            c.close()
            #print(f'File Saves in : {name}')



    fname=filedialog.asksaveasfilename(defaultextension='.txt')

    tk.Label(receive_file_window,text='Receving Files',bg='orange',fg='blue',font='Arial 15').pack(fill=tk.X)

     
    tk.Label(receive_file_window,text='Enter Device ID :',bg='skyblue').place(x=50,y=60)
    ip=tk.Entry(receive_file_window)
    ip.place(x=180,y=60)

    tk.Label(receive_file_window,text='Enter PORT :',bg='skyblue').place(x=50,y=100)
    port=tk.Spinbox(receive_file_window,from_=1024,to=65535)
    port.place(x=180,y=100) 

    
    
    


     
    """  tk.Label(receive_file_window,text='Name to Save:',bg='skyblue').place(x=50,y=150)
    f_name=tk.Entry(receive_file_window)
    f_name.place(x=150,y=150) """
    


    tk.Button(receive_file_window,text='Receive File',bg='red',fg='skyblue',font='Sarif 19',command=file_fun).place(x=100,y=230)
    



    
    receive_file_window.mainloop()
    receive_file_window.destroy()
    #Receive Filepath
    #filepath=c.recv(1024).decode()
    #path='/home/ubentu/Desktop/My Project/Chat/'+'james.txt'
    #receive Data
    #data=c.recv(1024).decode()
     
    
    
#=================================================================================

def send_image():
    
    global filepath


    root=tk.Tk()
    root.title('Sending Image')
    root.geometry('400x400')
    root.config(bg=bg_sub_window)


    def select_image():
        global filepath
        filepath=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetypes=(('JPG','.jpg'),('JPEG','.jpeg'),('PNG','png'),('BNG','.bng'))
                                            )
        #print(filepath)


    def send_image_fun():
        global filepath
        I=socket.gethostname()
        P=port.get()
        
        
        if (not str(P)):
            messagebox.showerror(title='Error !!',message='Please Enter Port !!')
        elif  (str(P) < str(1024))  : 
            messagebox.showerror(title='Error !!',message='Port Mustbe Above(1024)')

        elif (str(P) > str(65535)):
            messagebox.showerror(title='Error !!',message='Port Mustbe Below(65535) ')

        elif  (filepath == ""):
            messagebox.showerror(title='Error !!',message='Select Any file')


        elif  str(I) and str(P):
            s=socket.socket()
            s.bind((str(I),int(P)))
            s.listen()
            """ print(filepath)
            print(I,P)
            print('Listening..............') """
            c,addr=s.accept()
            messagebox.showinfo(title='User',message=f'Connected With { addr}')
            file=open(filepath,'rb')
            image_data=file.read(2048)#2mb
            while image_data:
                c.send(image_data)
                image_data=file.read(2048)
            messagebox.showinfo(title='Completed',message='Successfully Sending Completed')
            
            file.close()
            s.close()

    tk.Label(root,text='Sending Image',bg='orange',fg='blue',font='Arial 15').pack(fill=tk.X)
    tk.Button(root,text=' + Select Image',bg='green',fg='white',font='Sarif 15',command=select_image).place(x=120,y=180)
    tk.Label(root,text='Your Device ID :',bg=bg_sub_window).place(x=50,y=80)

    ip=tk.Label(root,text=f'{socket.gethostname()}',bg='blue',fg='white')
    ip.place(x=180,y=80)

    tk.Label(root,text='Set PORT :',bg=bg_sub_window).place(x=50,y=130)
    port=tk.Spinbox(root,from_=1024,to=65535)
    port.place(x=180,y=130)

     
    


    tk.Button(root,text='Send ',bg='red',fg='white',font='Sarif 15',command=send_image_fun).place(x=120,y=250)
    root.mainloop()

#================================================================================


def receive_image():

    fname=''
    root=tk.Tk()
    root.title('Receving Image')
    root.geometry('400x400')
    root.config(bg=bg_sub_window)

    def receive_image_fun():
        #print('Hello')
        I=ip.get()
        P=port.get()
        if (not I) and (not P) and (not fname):
            
            messagebox.showerror(title='Error !!',message='Some Fields Empty !!!')
        else: 
            c=socket.socket()
            c.connect((str(I),int(P)))
            file=open(fname,'wb')
            image_data=c.recv(2048)
            while image_data:
                file.write(image_data)
                image_data=c.recv(2048)
            messagebox.showinfo(title='',message=f'Image Received - {fname}')
            file.close()
            c.close()



    fname=filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                       title="Save to File",
                                       filetypes=(('JPG','.jpg'),('JPEG','.jpeg'),('PNG','.png')))

    tk.Label(root,text='Receving Image',bg='orange',fg='blue',font='Arial 15').pack(fill=tk.X)

    tk.Label(root,text='Enter Device ID :',bg=bg_sub_window).place(x=50,y=80)
    ip=tk.Entry(root)
    ip.place(x=180,y=80)

    tk.Label(root,text='Enter Device PORT :',bg=bg_sub_window).place(x=50,y=130)
    port=tk.Spinbox(root,from_=1024,to=65535)
    port.place(x=180,y=130)

    tk.Button(root,text='Receive Image',bg='red',fg='skyblue',font='Sarif 19',command=receive_image_fun).place(x=100,y=230)


    root.mainloop()


#=================================================================================

def help_fun():
    help=tk.Toplevel()
    help.title('Help Window')
    help.geometry('500x400')
    

    help.mainloop()
#==================================================================================

if __name__ == '__main__':
    btn_width=15
    btn_x=50
    btn_x_2=350
    send_btn_color='yellow'
    send_btn_fg='blue'
    bg='white'
    root=tk.Tk()
    root.title('WelCome To E-FTP Software')
    root.config(bg=bg)
    root.geometry('650x400')
    root.resizable(False,False)
    try :
        logo=Image.open('/home/ubentu/Pictures/LOGO.png')
        logo=logo.resize((50,50))
        logo=ImageTk.PhotoImage(logo)
        tk.Label(root,image=logo).place(x=0,y=0)
    except:
        pass
    
    title=tk.Label(root,text='E- FTP',bg='orange',fg='blue',font='Arial 31 bold',width=26)
    title.place(x=52,y=0)
    #------------------Sending Buttons---------------------
    send_files=tk.Button(root,text='Send Files',fg=send_btn_fg,bg=send_btn_color,font='Arial 20 bold',width=btn_width,command=send_file)
    send_files.place(x=btn_x,y=100)

    send_images=tk.Button(root,text='Send Images',fg=send_btn_fg,bg=send_btn_color,font='Arial 20 bold',width=btn_width,command=send_image)
    send_images.place(x=btn_x,y=150)
    
    send_videos=tk.Button(root,text='Send Videos',fg=send_btn_fg,bg=send_btn_color,font='Arial 20 bold',width=btn_width)
    send_videos.place(x=btn_x,y=200)

    send_camara=tk.Button(root,text='Send Camara',fg=send_btn_fg,bg=send_btn_color,font='Arial 20 bold',width=btn_width)
    send_camara.place(x=btn_x,y=250)



    #-----------------Receving Buttons------------------
    receive_files=tk.Button(root,text='Receive Files',fg='white',bg='blue',font='Arial 20 bold',width=btn_width,command=receive_file)
    receive_files.place(x=btn_x_2,y=100)

    receive_images=tk.Button(root,text='Receive Images',fg='white',bg='blue',font='Arial 20 bold',width=btn_width,command=receive_image)
    receive_images.place(x=btn_x_2,y=150)
    
    receive_videos=tk.Button(root,text='Receive Videos',fg='white',bg='blue',font='Arial 20 bold',width=btn_width)
    receive_videos.place(x=btn_x_2,y=200)

    receive_camara=tk.Button(root,text='Receive Camara',fg='white',bg='blue',font='Arial 20 bold',width=btn_width)
    receive_camara.place(x=btn_x_2,y=250)
    
    #------------------Help Button -----------------------
    
    Help=tk.Button(root,text='Help',fg='white',bg='green',font='Arial 20 bold',width=12,command=help_fun)
    Help.place(x=70,y=330)

    

    #------------------Exit Button -----------------------
    try :
        img=Image.open('/home/ubentu/Desktop/M Project/Chat/exit1.jpeg')
        img=img.resize((150,40))
        img=ImageTk.PhotoImage(img)
        #cv2.imshow('Image',img)
        #print(img)
        Exit=tk.Button(root,image=img,command=lambda: exit(),bg=bg,activebackground=bg,border=0)
        Exit.place(x=btn_x_2+50,y=330)
    except:
        Exit = tk.Button(root, text="Exit", command=lambda: exit(), bg='Red', activebackground=bg, font="Arial 20 bold",border=0)
        Exit.place(x=btn_x_2 + 50, y=330)


    root.mainloop()











