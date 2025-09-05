import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

active_networks=[]

def check_essid(essid,lst):
    check_status=True
    if len(lst) ==0:
        return check_status
    
    for item in lst:
        if essid in item["ESSID"]:
            check_status=False
        return check_status
    

if not 'SUDO_UID' in os.environ.keys():
    print('Try running this program with sudo.')
    exit()

for file_name in os.linesep():

    if ".csv" in file_name:
        print('There should not be any .csv')
        directory=os.getcwd()

        try:
            os.mkdir(directory+"/backup/")
        except:
            print("Backup Folder is Exists.")

        timestamp=datetime.now()
        shutil.move(file_name,directory+"/backup/"+str(timestamp) +"hello.csv")
wlan_pattren=re.compile("^wlan[0-9]+")

check_wifi_result=wlan_pattren.findall(subprocess.run(["iwconfig"],capture_output=True))

if len(check_wifi_result) == 0:
    print("Please connect a Wifi adapter and try again.")
    exit()

print('The Following Wifi InterFaces :')
for index,item in enumerate(check_wifi_result):
    print(f"{index} - {item}")




while True:
    wifi_interface_choice=input('Please select interface :')
    try:
        if check_wifi_result(int(wifi_interface_choice)):
            break
    except:
        print("Please enter a number thar corresponding:")

hacknic=check_wifi_result[int(wifi_interface_choice)]

print("Wifi Adapter Connected ! \n Now let's kill confilcting Processes:")


kill_con_proc=subprocess.run(["sudo","airmon-ng","check","kill"])

print('Putting wifi Adapter into moniter Mode:')
put_in_mon_mode=subprocess.run(["sudo","airmon-ng","start",hacknic])

dis_access_points=subprocess.run(["sudo","airodump-ng","-w","file","--write-interval","1","--output-format","csv",check_wifi_result[0] + "mon"],stdout=subprocess.DEVNULL)




