import tkinter as tk
 
window = tk.Tk()
window.geometry("450x300")
window.configure(bg="#ADD8E6")
window.title("Student Login Form")
#heading
label = tk.Label(text="Login Here ",font=( "Arial",12),fg="blue", width=10, height=2)#font=("Arial",10))
label.grid(row=1,column=2)

#login field
user_label=tk.Label(text="Username :", fg= "white" , bg="green",font=( "Arial",12), width=20)
user_label.grid(row=5, column=1)
#password field
pass_label=tk.Label(text="Password :", fg= "white", bg="green" ,font=( "Arial",12) , width=20)
pass_label.grid(row=7, column=1)

# username input
username_1=tk.Entry(fg="blue", bg="white",width=37 )
username_1.grid(row=5, column=2)
#password input
password_1=tk.Entry(fg="blue", bg="white", width=37)
password_1.grid(row=7, column=2)
 
def clicked():
    username=username_1.get()
    password=password_1.get()
    #print(username)
    #print(password)

    data=open('/home/ubentu/Desktop/My Project/Normal/result.txt','a')
    #print(data.read())
    data.write(username)
    data.write(password)
    data.close()
    
    f=open('/home/ubentu/Desktop/My Project/Normal/result.txt','r')
    print(f.read())
    f.close()



 
button=tk.Button(text="Login", font=( "Arial",13),fg="white", bg="red", width=25,  command=clicked)
button.grid(row=10,column=2)
 
window.mainloop()
