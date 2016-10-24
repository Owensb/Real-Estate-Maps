#tutorial for PANDA

import pandas as pd #this is the standard
import matplotlib.pyplot as plt
import matplotlib.cm
import json
import googlemaps
from datetime import datetime



df = pd.read_csv('Single Line.csv', header=0 )
df.columns = ['number', 'mls_ID','Status', 'Area', 'Address', 'Beds', 'Baths_Full',  'Baths_Half',  'Stories'  , 'Parking_Spaces' , 'Garage', 'Pets', 'Year_Built', 'Sqft_Total', 'LP$SqFt', 'List_Price', 'Sold/Lease$/SqFt','Sold/Lease_Price' , 'Sold/Lease_Date' , 'ADOM' , 'CDOM']
df.index= ['0','1' ,'2', '3','4','5','6','7','8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
# getting first x rows
id_col = df.pop('number')
id_col = df.pop('Status')
id_col = df.pop('Garage')
id_col = df.pop('Stories')
id_col = df.pop('Area')
id_col = df.pop('mls_ID')
id_col = df.pop('Sold/Lease$/SqFt')
id_col = df.pop('Sold/Lease_Price')
id_col = df.pop('Sold/Lease_Date')
id_col = df.pop('Pets')
id_col = df.pop('ADOM')
id_col = df.pop('CDOM')
id_col = df.pop('Parking_Spaces')
id_col = df.pop('Year_Built')
# id_row = df.drop('12')
df = df[df.index != '12']
df.head()

df1=[]

gmaps = googlemaps.Client(key='AIzaSyAWJ5qYyCK3CdF9NwYpJJIrccV0kQaYvbo')

# Geocoding all the addresses
for list in df['Address']:
	address = list
	geocode_result = gmaps.geocode(list + ", TX")
	lat=([s['geometry']['location']['lat'] for s in geocode_result])
	lng=([s['geometry']['location']['lng'] for s in geocode_result])
	

	df1.append({'Address': address, 'Lat': lat, 'Lng' : lng })
	latlng=pd.DataFrame(df1)
	latlng.columns = ['Address', 'Latitude', "Lng"]
	latlng.head()


df= df.merge(latlng, on='Address')

print(df)
df.head()

df.to_csv('property_locations')
