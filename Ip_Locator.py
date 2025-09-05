import ipaddress
import requests

import imps
#pip install imps
import tkintermapview
#pip install tkintermapview

import tkinter as tk


from tkinter import ttk
from tkinter import *
#from tkinter.ttk import *


#
#-------------------------------------------#
#


def ipFinder(output,inputValue):
    
    print(inputValue)
    try:
        ipAddress=inputValue.get()
        ipaddress.ip_address(ipAddress)
        response=requests.get(f'https://ipapi.co/{ipAddress}/json/').json()
        ip_version=response.get('version')
        city=response.get('city')
        region=response.get('region')
        country=response.get('country_name')
        postlcode=response.get('postal')
        continent=response.get('continent_code')
        lat=response.get('latitude')
        lng=response.get('longitude')
        output.config(text="Information for "+inputValue.get() +":" + "\n"+
                            "Ip Verion" + ":" +str(ip_version) + "\n" +
                            "City" + ":" +str(city) + "\n"+
                            "Region" + ":" +str(region) + "\n"+
                            "Country" + ":" +str(country) + "\n"+
                            "Postlcode" + ":" +str(postlcode) + "\n"+
                            "Continent" + ":" +str(continent) + "\n"+
                            "Latitude" + ":" +str(lat) + "\n"+
                            "Longitude" + ":" +str(lng) + "\n"
                            "--------------------------")



                    



    except:
        pass


        





#
#-------------------------------------------#
#



root=Tk()
root.geometry("800x500")
root.resizable(False,False)

root.title("IP ADDRESS ")
root.configure(bg="blue")

label=Label(root,text="IP",bg="white",fg="red",font="arial 20 bold")
label.pack(fill=X,pady=3)

inputString=StringVar()

#Label Place
entry_label=Label(root,text="Enter IP :",fg='white',bg="blue",font="arial 12")
entry_label.place(x=40,y=60)

#Entry palce
input_entry=Entry(root,textvariable=inputString,font="arial 13")
input_entry.place(x=100,y=60)

#Output message

output=Label(root,background="white",fg="black")
output.place(x=40,y=100)




#Button to find ip address
button=Button(root,text="Find",fg='white',bg='gray',command=lambda: ipFinder(output,inputString),width=16)
button.place(x=310,y=460)

#Zoom [in] and Zoom [out] Slider

slider=Scale(root,from_=2,to=20,orient=HORIZONTAL,command="",length=200)
slider.place(x=470,y=460)








root.mainloop()

