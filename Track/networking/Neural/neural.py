import sys
import phonenumbers
from phonenumbers import geocoder
import folium
import opencage.geocoder
Key = "bb3e361bd1f14bf9976076d864faec0c"
number = input("Phone Number: ")
ch_number = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(ch_number, "en")
print(location)
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number,"en"))
samNumber = phonenumbers.parse(number)
from opencage.geocoder import OpenCageGeocoder
geocoder = OpenCageGeocoder(Key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)
myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to((myMap))

myMap.save('myLocation.html')