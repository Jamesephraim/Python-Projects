import phonenumbers
import folium
from phonenumbers import geocoder
#pip install phonenumbers
#pip install folium


 
#Logo Design 
print(' ______   __    __   ______   ___     __   ______   __   ___     __   _______   ______')
print('|  __  | |  |  |  | |  __  | |   \   |  | |  ____| |  | |   \   |  | |   ____| |  __  |') 
print('| |__| | |  |  |  | | |  | | |    \  |  | | |      |  | |    \  |  | |  |      | |  | |')
print('|  ____| |  |__|  | | |  | | |  |\ \ |  | | |____  |  | |  |\ \ |  | |  |____  | |  | |')
print('| |	    |   __   | | |  | | |  | \ \|  | |  ____| |  | |  | \ \|  | |   ____| | |  | |')
print('| |      |  |  |  | | |  | | |  |  \    | | |      |  | |  |  \ |  | |  |      | |  | |')
print('| |      |  |  |  | | |__| | |  |   \   | | |____  |  | |  |   \   | |  |      | |__| |')
print('|_|	    |__|  |__| |______| |__|    \__| |______| |__| |__|    \__| |__|      |______|')


#Take A mobile Number
number=input("Enter A Phone Number and Country Code :")
#Find Country in the mobile number
country= phonenumbers.parse(number)
location=geocoder.description_for_number(country,"en")

from phonenumbers import carrier
service=phonenumbers.parse(number)

 

#Display the Country
print('[+] Country :',geocoder.description_for_number(country,"en"))

#Display the Service Provider
print('[+] Service :',carrier.name_for_number(service,'en'))

from opencage.geocoder import OpenCageGeocode
key='114fc46066544cdcb89800f988c228ca'
geocoder=OpenCageGeocode(key)
q=str(location)
results=geocoder.geocode(q)
#print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print('[+] Lat',lat)
print('[+] Lon',lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)


myMap.save("Mylocation.html")
